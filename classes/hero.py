import math, time
from equipment import weapons as w
from equipment import armor as a
from equipment import specials as s
from equipment import potions
from equipment import scrolls
from classes import dice


def pick_class(name):
    print("\nNext, pick a class:")

    class_list = ["Fighter", "Rogue", "Wizard", "Wanderer"]

    class_name = "Null"
    while class_name not in class_list:
        print(", ".join(class_list))
        class_name = input(">> ")
        class_name = class_name.capitalize()
    if class_name == "Fighter":
        return Fighter(name=name)
    elif class_name == "Rogue":
        return Rogue(name=name)
    elif class_name == "Wizard":
        return Wizard(name=name)
    elif class_name == "Wanderer":
        return WandererStats(name)
    else:
        print("Class Picking Error")
        exit(1)


def WandererStats(name):
    print("\nWelcome, Wanderer. Let's assign your stats:")
    stats = ["15", "13", "12", "11", "10", "9"]

    time.sleep(1)
    
    strength = ""
    while strength not in stats:
        print("\nWhat is your Strength?")
        print(", ".join(stats))
        strength = input(">> ")
    stats.remove(strength)

    dex = ""
    while dex not in stats:
        print("\nWhat is your Dexterity?")
        print(", ".join(stats))
        dex = input(">> ")
    stats.remove(dex)

    con = ""
    while con not in stats:
        print("\nWhat is your Constitution?")
        print(", ".join(stats))
        con = input(">> ")
    stats.remove(con)

    wis = ""
    while wis not in stats:
        print("\nWhat is your Wisdom?")
        print(", ".join(stats))
        wis = input(">> ")
    stats.remove(wis)

    intelligence = ""
    while intelligence not in stats:
        print("\nWhat is your Intelligence?")
        print(", ".join(stats))
        intelligence = input(">> ")
    stats.remove(intelligence)

    cha = ""
    while cha not in stats:
        print("\nWhat is your Charisma?")
        print(", ".join(stats))
        cha = input(">> ")
    stats.remove(cha)

    return Wanderer(name=name, str=int(strength), dex=int(dex), con=int(con), wis=int(wis), int=int(intelligence), cha=int(cha))


class Hero:
    """basic player hero class"""

    def __init__(self, name="Hero", class_name="Hero", class_level=1, base_health=10, xp=0, weapon=w.Unarmed(), inventory=[], special=[], armor=a.Leather(), str=10, dex=10, con=10, int=10, wis=10, cha=10, max_health=0, health=0, gold=0, in_fight=False, cooldown=0):
        self.name = name
        self.class_name = class_name
        self.class_level = class_level
        self.xp = xp
        self.weapon=weapon
        self.armor = armor
        self.inventory = inventory
        self.special = special
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.ac = 0
        self.update_ac()
        self.base_health = base_health
        self.max_health = 0
        self.health = health
        if max_health == 0:
            self.initial_health()
        else:
            self.max_health = max_health
        self.gold = gold
        self.alive = True
        self.prof = 0
        self.update_prof_bonus()
        self.in_fight = in_fight
        self.cooldown = cooldown

    def attack(self, enemy: object, enemies_in_fight: list):
        roll = dice.roll(1, 20)
        attack_roll = roll + self.stat_mod(self.str) + self.prof

        if roll == 20:
            print("Critical!")
            enemy.take_damage(self.do_damage(True, self.stat_mod(self.str)))
        elif attack_roll > enemy.ac:
            enemy.take_damage(self.do_damage(False, self.stat_mod(self.str)))
        else:
            print(self.name, "missed", enemy.name)
  
    def check_for_level_up(self, threshold: int):
        if self.xp >= threshold:
            return True
        else:
            return False

    def check_inventory(self):
        inventory_cap = 5 + self.stat_mod(self.str)
        while len(self.inventory) > inventory_cap:
            print("\nToo many items, pick one to discard:")
            print(", ".join(self.inventory))

            choice = ""
            while choice not in self.inventory:
                choice = input(">> ")
            self.inventory.remove(choice)

    def do_damage(self, crit: bool, stat_mod: int):
        damage = 0
        if crit == True:
            damage = dice.roll(self.weapon.num_damage_dice, self.weapon.damage_die) + dice.roll(
                self.weapon.num_damage_dice, self.weapon.damage_die) + stat_mod
        else:
            damage = dice.roll(self.weapon.num_damage_dice,
                               self.weapon.damage_die) + stat_mod

        return damage

    def gain_xp(self, xp: int):
        mod = self.stat_mod(self.int)
        if mod >= 0:
            self.xp += xp + mod
        else:
            self.xp += xp

        threshold = 7 + self.class_level
        while self.check_for_level_up(threshold):
            self.xp -= threshold
            self.level_up()

    def heal(self, divisor=2):
        heal = math.floor(self.max_health/divisor)
        if self.health + heal >= self.max_health:
            self.health = self.max_health
        else:
            self.health += heal

    def increase_level(self):
        self.class_level += 1
    
    def increase_stat(self, choice: str):
        if choice == "str":
            self.str += 1
        elif choice == "dex":
            self.dex += 1
            self.update_ac()
        elif choice == "con":
            self.con += 1
            if self.con % 2 == 0:
                self.update_health(1 * self.class_level)
        elif choice == "int":
            self.int += 1
        elif choice == "wis":
            self.wis += 1
        elif choice == "cha":
            self.cha += 1

    def initial_health(self):
        self.max_health = (self.stat_mod(self.con)
                           * self.class_level) + self.base_health + (dice.roll(self.class_level-1, self.base_health))
        self.health = self.max_health

    def level_up(self):
        print("\n\nLevel Up!")
        print("Pick a stat to increase:")
        attr_dic = {"str": self.str, "dex": self.dex,
                    "con": self.con, "int": self.int,
                    "wis": self.wis, "cha": self.cha}

        for stat in attr_dic:
            print(stat + ": " + str(attr_dic[stat]))
            print(stat + " mod: " + str(self.stat_mod(attr_dic[stat])))

        choice = "null"
        while choice not in attr_dic or attr_dic[choice] >= 20:
            print("\nPlease pick a stat whose value is less than 20")
            choice = input(">> ")

        self.increase_stat(choice)
        self.increase_level()
        self.update_health(dice.roll(1, self.base_health) +
                           self.stat_mod(self.con))
        self.update_prof_bonus()

    def show_inventory(self, player_turn, enemies_in_fight: list):
        cure_light = potions.Cure_Light()
        cure_moderate = potions.Cure_Moderate()
        cure_serious = potions.Cure_Serious()
        scroll_escape = scrolls.Escape()

        print("\nInventory:")
        print("\n".join(self.inventory))
        print("back")

        choice = ""
        while choice not in self.inventory and choice.lower() != "back":
            choice = input(">> ")

        if choice in self.inventory:
            if choice == "cure light potion":
                cure_light.heal(self)
            elif choice == "cure moderate potion":
                cure_moderate.heal(self)
            elif choice == "cure serious potion":
                cure_serious.heal(self)
            elif choice == "scroll of escape":
                scroll_escape.escape(self)
            self.inventory.remove(choice)
        elif choice == "back":
            player_turn(self, enemies_in_fight)

    def show_specials(self, enemy: object, enemies_in_fight: list, player_turn):
        if self.cooldown <= 0:
            print("Special Moves:")
            special_list = []
            for special in self.weapon.special:
                special_list.append(special)
            for special in self.special:
                if special not in special_list:
                    special_list.append(special)
            special_list.sort()
            print("\n".join(special_list))
            print("back")

            choice = ""
            while choice.lower() not in special_list and choice.lower() != "back":
                choice = input(">> ")
            
            if choice.lower() == "cleave":
                s.cleave(self, enemy, enemies_in_fight)
                self.cooldown = 4
            elif choice.lower() == "fireball":
                s.fireball(self, enemies_in_fight)
                self.cooldown = 4
            elif choice.lower() == "double strike":
                s.double_strike(self, enemy, enemies_in_fight)
                self.cooldown = 4
            elif choice.lower() == "flurry":
                s.flurry(self, enemies_in_fight)
                self.cooldown = 4
            elif choice.lower() == "magic missile":
                s.magic_missile(self, enemy)
                self.cooldown = 4
            elif choice.lower() == "back stab":
                s.back_stab(self, enemy)
                self.cooldown = 4
            elif choice.lower() == "back":
                player_turn(self, enemies_in_fight)
            else:
                print("Special Attack Choice Error!")
                exit(1)
        else:
            print("Special on cooldown for {} more turns".format(
                self.cooldown))
            player_turn(self, enemies_in_fight)

    def stat_mod (self, stat: int):
        return math.floor((stat - 10)/2)

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
        print("{0.name} took {1} damage, and have {0.health} hit points left".format(
            self, damage))

    def update_ac(self):
        self.ac = 10 + self.stat_mod(self.dex) + \
            self.armor.value + self.armor.magic

    def update_health(self, amount: int):
        self.max_health += amount
        self.health = self.max_health
        
    def update_prof_bonus(self):
        self.prof = math.floor(self.class_level/4)+2


class Fighter(Hero):
    """tank based class"""

    def __init__(self, name="Hero", class_name="Fighter", class_level=1, base_health=10, weapon=w.LongSword(), inventory=["cure light potion"], special=["cleave"], armor=a.Leather(), str=15, dex=12, con=13, int=10, wis=11, cha=9, max_health=0, health=0, gold=0, cooldown=0):
        self.name = name
        self.class_name = class_name
        self.class_level = class_level
        self.xp = 0
        self.weapon = weapon
        self.armor = armor
        self.inventory = inventory
        self.special = special
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.ac = 0
        self.update_ac()
        self.base_health = base_health
        self.health = health
        if max_health == 0:
            self.initial_health()
        else:
            self.max_health = max_health
        self.prof = 0
        self.update_prof_bonus()
        self.gold = gold
        self.alive = True
        self.cooldown = cooldown


class Rogue(Hero):
    """evasion and critical damage based class"""

    def __init__(self, name="Hero", class_name="Rogue", class_level=1, base_health=6, weapon=w.ShortSword(), inventory=["cure light potion", "scroll of escape"], special=["back stab"], armor=a.Leather(), str=9, dex=15, con=13, int=11, wis=10, cha=12, health=0, max_health=0, gold=0, cooldown=0):
        self.name = name
        self.class_name = class_name
        self.class_level = class_level
        self.xp = 0
        self.weapon = weapon
        self.armor = armor
        self.inventory = inventory
        self.special = special
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.ac = 0
        self.update_ac()
        self.base_health = base_health
        self.health = health
        if max_health == 0:
            self.initial_health()
        else:
            self.max_health = max_health
        self.prof = 0
        self.update_prof_bonus()
        self.gold = gold
        self.alive = True
        self.cooldown = cooldown

    def attack(self, enemy: object, enemies_in_fight: list):
        roll = dice.roll(1, 20)
        attack_roll = roll + self.stat_mod(self.dex)

        if roll >= 18:
            print("Critical!")
            enemy.take_damage(self.do_damage(True, self.stat_mod(self.str)))
        elif attack_roll > enemy.ac:
            enemy.take_damage(self.do_damage(False, self.stat_mod(self.str)))
        else:
            print(self.name, "missed", enemy.name)

    def take_damage(self, damage: int):
        dodge_chance = dice.roll(1, 100)
        if dodge_chance > 30:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.alive = False
            print("{0.name} took {1} damage, and have {0.health} hit points left".format(self, damage))
        else:
            print(self.name, "dodged the attack")


class Wizard(Hero):
    """Fast leveling, AoE based class"""

    def __init__(self, name="Hero", class_name="Wizard", class_level=1, weapon=w.Staff(), inventory=["cure light potion", "scroll of escape"], special=["magic missile"], armor=a.Hide(), base_health=4, str=9, dex=12, con=13, int=15, wis=11, cha=10, health=0, max_health=0, gold=0, cooldown=0):
        self.name = name
        self.class_name = class_name
        self.class_level = class_level
        self.xp = 0
        self.weapon = weapon
        self.armor = armor
        self.inventory = inventory
        self.special = special
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.ac = 0
        self.update_ac()
        self.base_health = base_health
        self.health = health
        if max_health == 0:
            self.initial_health()
        else:
            self.max_health = max_health
        self.prof = 0
        self.update_prof_bonus()
        self.gold = gold
        self.alive = True
        self.cooldown = cooldown

    def attack(self, enemy: object, enemies_in_fight: list):
        """target up to 3 enemies"""
        targets = []

        # if 3 or fewer foes, attack all foes
        if len(enemies_in_fight) < 4: 
            targets = enemies_in_fight
        else:
            enemy_index = enemies_in_fight.index(enemy)

            # first target
            enemy1 = None
            if enemy_index - 1 >= 0:
                enemy1 = enemies_in_fight[enemy_index - 1]
            else:
                enemy1 = enemies_in_fight[-1]
            
            # second target
            enemy2 = enemy

            # third target
            enemy3 = None
            if enemy_index + 1 <= len(enemies_in_fight) - 1:
                enemy3 = enemies_in_fight[enemy_index + 1]
            else:
                enemy3 = enemies_in_fight[0]
            
            targets = [enemy1, enemy2, enemy3]
            
        # attack the enemies
        for target in targets:
            roll = dice.roll(1, 20)
            attack_roll = roll + self.stat_mod(self.int)
            if roll == 20:
                target.take_damage(self.do_damage(
                    True, self.stat_mod(self.str)))
            elif attack_roll > target.ac:
                target.take_damage(self.do_damage(
                    False, self.stat_mod(self.str)))
            else:
                print(self.name, "missed", target.name)


class Wanderer(Hero):
    """basic blank slate"""

    def __init__(self, name="Hero", class_name="Wanderer", class_level=1, weapon=w.Unarmed(), inventory=["cure moderate potion"], special=["double strike"], armor=a.Leather(), base_health=8, str=10, dex=10, con=10, int=10, wis=10, cha=10, health=0, max_health=0, gold=0, cooldown=0):
        self.name = name
        self.class_name = class_name
        self.class_level = class_level
        self.xp = 0
        self.weapon = weapon
        self.armor = armor
        self.inventory = inventory
        self.special = special
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.ac = 0
        self.update_ac()
        self.base_health = base_health
        self.health = health
        if max_health == 0:
            self.initial_health()
        else:
            self.max_health = max_health
        self.prof = 0
        self.update_prof_bonus()
        self.gold = gold
        self.alive = True
        self.cooldown = cooldown


