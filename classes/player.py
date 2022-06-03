import math

class Util:
    def pick_class(self):
        print("\nNext, pick a class:")

        class_list = ["Fighter", "Rogue", "Wizard", "Wanderer"]

        class_name = "Null"
        while class_name not in class_list:
            print(", ".join(class_list))
            class_name = input(">> ")
            class_name = class_name.capitalize()
        return class_name

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
    
        self.increase_stat(choice)
        self.increase_level()
    
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
    
