import classes.player as player
import classes.misc as misc

print("Welcome, hero! What are you called?")
name = input(">> ")

print("\nNext, pick a class:")
class_list = ["Fighter", "Rogue", "Wizard"]

class_name = "Null"
while class_name not in class_list:
    print(", ".join(class_list))
    class_name = input(">> ")
    class_name = class_name.capitalize()

hero = player.Hero(name=name, class_name=class_name)

print() 

attr_dic = {"Name": hero.name, "Class": hero.class_name,
            "Level": hero.level, "HP": hero.health,
            "str": hero.str, "dex": hero.dex, "con": hero.con}

for stat in attr_dic:
    print(stat + " : " + str(attr_dic[stat]))

hero.level_up()

print()

for stat in attr_dic:
    print(stat + " : " + str(attr_dic[stat]))

input("[Enter]")
print()

hero2 = player.Hero(name="Sean", class_name="Fighter", con=18)

attr_dic = {"Name": hero2.name, "Class": hero2.class_name,
            "HP": hero2.health, "str": hero2.str, "dex": hero2.dex, "con": hero2.con}

for stat in attr_dic:
    print(stat + " : " + str(attr_dic[stat]))

input("[Enter]")
print()

misc_roll = misc.Misc()
print("How many time would you like to roll 1d20?")
num = input(">> ")
print("Rolling 1d20 " + str(num) + " times: ")
for i in range(int(num)):
    print(str(misc_roll.roll(1, 20)))

