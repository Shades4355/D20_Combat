import random


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

    def roll(self, num, die):
        total = 0
        for i in range(0, num):
            total += random.randrange(1, die + 1)
        return round(total)
