import math
import classes.utility_functions as utils

# player hero classes
class Hero:
    def __init__(self, name="Hero", class_name="Fighter", base_health=10, xp=0, str=10, dex=10, con=10, int=10, wis=10, cha=10):
        self.name = name
        self.class_name = class_name
        self.class_level = 1
        self.xp = xp
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.base_health = base_health
        self.health = self.base_health
        self.update_health()
    
    def stat_mod (self, stat):
        return math.floor((stat - 10)/2)

    def increase_level(self):
        self.class_level += 1
    
    def update_health(self):
        self.health = (self.stat_mod(self.con)
                        * self.class_level) + self.base_health

    def increase_stat(self, choice):
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
        util_functions = utils.Util()
        self.health += util_functions.roll(1, self.base_health)
    
    def gain_xp(self, xp):
        self.xp += xp
        threshold = 7 + self.class_level
        while self.check_for_level_up(threshold):
            self.level_up()
            self.xp -= threshold

    def check_for_level_up(self, threshold):
        if self.xp >= threshold:
            return True
        else:
            return False
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, stat):
        util_functions = utils.Util()
        return util_functions.roll(1,20) + self.stat_mod(stat)


# tank based class
class Fighter(Hero):
    def __init__(self, name="Hero", class_name="Fighter", base_health=10, xp=0, str=15, dex=12, con=13, int=9, wis=10, cha=11):
        super().__init__(name, class_name, base_health, xp, str, dex, con, int, wis, cha)


# evasion and critical damage based class
class Rogue(Hero):
    def __init__(self, name="Hero", class_name="Rogue", base_health=6, xp=0, str=9, dex=15, con=13, int=11, wis=10, cha=12):
        super().__init__(name, class_name, base_health, xp, str, dex, con, int, wis, cha)
   
    def take_damage(self, damage):
        util_func = utils.Util()
        dodge_chance = util_func.roll(1, 100)
        if dodge_chance > 25:
            self.health -= damage
            if self.health < 0:
                self.health = 0


# AoE based class
class Wizard(Hero):
    def __init__(self, name="Hero", class_name="Wizard", base_health=4, xp=0, str=10, dex=10, con=10, int=10, wis=10, cha=10):
        super().__init__(name, class_name, base_health, xp, str, dex, con, int, wis, cha)


# basic blank slate
class Wanderer(Hero):
    def __init__(self, name="Hero", class_name="Wanderer", base_health=8, xp=0, str=10, dex=10, con=10, int=10, wis=10, cha=10):
        super().__init__(name, class_name, base_health, xp, str, dex, con, int, wis, cha)
