import math
from unittest import case

# player hero class
class Hero:
    def __init__(self, name="Hero", class_name="fighter", xp=0, str=10, dex=10, con=10, int=10, wis=10, cha=10):
        self.health_by_class = {
            "Fighter": 10,
            "Rogue": 6,
            "Wizard": 4
        }
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
        self.base_health = self.health_by_class[class_name]
        self.health = self.base_health
        self.update_health()
    
    def stat_mod (self, stat):
        return (stat - 10)/2

    def level_up_stat(self, stat):
        stat += 1
    
    def update_health(self):
        self.health = (round(
                        (self.stat_mod(self.con))
                        * (self.class_level))) + self.base_health

    def increase_stat(self, choice):
        if choice == "str":
            self.level_up_stat(self.str)
        elif choice == "dex":
            self.level_up_stat(self.dex)
        elif choice == "con":
            self.level_up_stat(self.con)
            self.update_health()
        elif choice == "int":
            self.level_up_stat(self.int)
        elif choice == "wis":
            self.level_up_stat(self.wis)
        elif choice == "cha":
            self.level_up_stat(self.cha)

    def level_up(self):
        print("Pick a stat to increase:")
        attr_dic = {"str": self.str, "dex": self.dex,
                    "con": self.con, "int": self.int,
                    "wis": self.wis, "cha": self.cha}

        for stat in attr_dic:
            print(stat + ": " + str(attr_dic[stat]))
            print(stat + " mod: " + str(round(self.stat_mod(attr_dic[stat]))))
        
        choice = "null"
        stat_dic = {"con": self.con}
        while choice not in stat_dic or attr_dic[choice] == 20:
            print("\nPlease pick a stat whose value is less than 20")
            choice = input(">> ")
    
        self.level_up_stat(self.class_level)
        self.increase_stat(choice)
    
    def gain_xp(self, xp):
        self.xp += xp
        while self.check_for_level_up():
            self.level_up()

    def check_for_level_up(self):
        if self.xp >= 7 + self.class_level:
            return True
        else:
            return False

    def gain_xp(self, amount):
        self.xp += amount