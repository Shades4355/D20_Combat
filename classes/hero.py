import math
from equipment import weapons as w
import classes.utility_functions as utils
dice = utils.Util()

class Pick_Class:
    def pick_class(self, name):
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
            return Wanderer(name=name)
        else:
            print("Class Picking Error")
            exit(1)

class Hero:
    """basic player hero class"""
    def __init__(self, name="Hero", class_name="Fighter", base_health=10, xp=0, weapon=w.Unarmed(), inventory=[], special=[], str=10, dex=10, con=10, int=10, wis=10, cha=10, gold=0):
        self.name = name
        self.class_name = class_name
        self.class_level = 1
        self.xp = xp
        self.weapon=weapon
        self.inventory = inventory
        self.special = special
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.base_health = base_health
        self.max_health
        self.health
        self.update_health()
        self.gold = gold
        self.alive = True
    
    def stat_mod (self, stat: int):
        return math.floor((stat - 10)/2)

    def increase_level(self):
        self.class_level += 1
    
    def update_health(self):
        self.max_health = (self.stat_mod(self.con)
                        * self.class_level) + self.base_health
        self.health = self.max_health

    def increase_stat(self, choice: str):
        if choice == "str":
            self.str += 1
        elif choice == "dex":
            self.dex += 1
        elif choice == "con":
            self.con += 1
            self.update_health()
        elif choice == "int":
            self.int += 1
        elif choice == "wis":
            self.wis += 1
        elif choice == "cha":
            self.cha += 1

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
    
        self.increase_level()
        self.increase_stat(choice)
        self.health += dice.roll(1, self.base_health)
    
    def gain_xp(self, xp: int):
        self.xp += xp
        threshold = 7 + self.class_level
        while self.check_for_level_up(threshold):
            self.level_up()
            self.xp -= threshold

    def check_for_level_up(self, threshold: int):
        if self.xp >= threshold:
            return True
        else:
            return False
    
    def take_damage(self, damage: int):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            self.alive = False
        print("{} took {} damage, and have {} hit points left".format(self.name, damage, self.current_health))

    def attack(self, enemy: object, enemies_in_fight: list):
        roll = dice.roll(1, 20)
        attack_roll = roll + self.stat_mod(self.str)

        if roll == 20:
            enemy.take_damage(self.do_damage(True))
        elif attack_roll > enemy.ac:
            enemy.take_damage(self.do_damage(False))
        else:
            print(self.name, "missed", enemy.name)

    def do_damage(self, crit: bool):
        damage = 0
        if crit == True:
            damage = dice.roll(self.weapon.num_damage_dice, self.weapon.damage_die) + dice.roll(self.weapon.num_damage_dice, self.weapon.damage_die) + self.stat_mod(self.str)
        else:
            damage = dice.roll(self.weapon.num_damage_dice, self.weapon.damage_die) + self.stat_mod(self.str)
        
        return damage


class Fighter(Hero):
    """tank based class"""
    def __init__(self, name="Hero", class_name="Fighter", base_health=10, xp=0, weapon=w.LongSword(), inventory=[], special=[], str=15, dex=12, con=13, int=10, wis=11, cha=9, gold=0):
        self.name = name
        self.class_name = class_name
        self.class_level = 1
        self.xp = xp
        self.weapon = weapon
        self.inventory = inventory
        self.special = special
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.base_health = base_health
        self.max_health
        self.health
        self.update_health()
        self.gold = gold
        self.alive = True


class Rogue(Hero):
    """evasion and critical damage based class"""
    def __init__(self, name="Hero", class_name="Rogue", base_health=6, weapon=w.ShortSword, str=9, dex=15, con=13, int=11, wis=10, cha=12):
        super().__init__(name, class_name, weapon, base_health, str, dex, con, int, wis, cha)
   
    def take_damage(self, damage: int):
        dodge_chance = dice.roll(1, 100)
        if dodge_chance > 25:
            self.health -= damage
            if self.health < 0:
                self.health = 0
                self.alive = False

    def attack(self, enemy: object, enemies_in_fight: list):
        roll = dice.roll(1, 20)
        attack_roll = roll + self.stat_mod(self.str)

        if roll >= 18:
            enemy.take_damage(self.do_damage(True))
        elif attack_roll > enemy.ac:
            enemy.take_damage(self.do_damage(False))
        else:
            print(self.name, "missed", enemy.name)


class Wizard(Hero):
    """AoE based class"""

    def __init__(self, name="Hero", class_name="Wizard", weapon=w.Staff(), base_health=4, str=10, dex=10, con=10, int=10, wis=10, cha=10):
        super().__init__(name, class_name, base_health, weapon, str, dex, con, int, wis, cha)

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
        for enemies in targets:
            roll = dice.roll(1, 20)
            attack_roll = roll + self.stat_mod(self.str)
            if roll == 20:
                enemies.take_damage(self.do_damage(True))
            elif attack_roll > enemy.ac:
                enemies.take_damage(self.do_damage(False))
            else:
                print(self.name, "missed", enemy.name)


class Wanderer(Hero):
    """basic blank slate"""
    def __init__(self, name="Hero", class_name="Wanderer", base_health=8, str=10, dex=10, con=10, int=10, wis=10, cha=10):
        super().__init__(name, class_name, base_health, str, dex, con, int, wis, cha)
