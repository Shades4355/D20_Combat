import random
import classes.hero as hero

class Util:
    def pick_class(self, name):
        print("\nNext, pick a class:")

        class_list = ["Fighter", "Rogue", "Wizard", "Wanderer"]

        class_name = "Null"
        while class_name not in class_list:
            print(", ".join(class_list))
            class_name = input(">> ")
            class_name = class_name.capitalize()
        if class_name == "Fighter":
            return hero.Fighter(name=name)
        elif class_name == "Rogue":
            return hero.Rogue(name=name)
        elif class_name == "Wizard":
            return hero.Wizard(name=name)
        elif class_name == "Wanderer":
            return hero.Wanderer(name=name)
        else:
            print("Class Picking Error")
            exit(1)

    def roll(self, num, die):
        total = 0
        for i in range(0, num):
            total += random.randrange(1, die + 1)
        return round(total)
