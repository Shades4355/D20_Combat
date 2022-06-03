import classes.player as player

print("Welcome, hero! What are you called?")
name = input(">> ")

util = player.Util()
class_name = util.pick_class()

hero = player.Hero(name=name, class_name=class_name)

print() 

attr_dic = {"Name": hero.name, "Class": hero.class_name,
            "Level": hero.class_level, "HP": hero.health,
            "str": hero.str, "dex": hero.dex, "con": hero.con}

print()

for stat in attr_dic:
    print(stat + " : " + str(attr_dic[stat]))

input("[Enter]")
print()

hero.gain_xp(25)

print()

attr_dic2 = {"Name": hero.name, "Class": hero.class_name,
            "Level": hero.class_level, "HP": hero.health,
            "str": hero.str, "dex": hero.dex, "con": hero.con}

for stat in attr_dic2:
    print(stat + " : " + str(attr_dic2[stat]))

input("[Enter]")
print()

util_functions = player.Util()
print("How many time would you like to roll 1d20?")
num = input(">> ")
print("Rolling 1d20 " + str(num) + " times: ")
for i in range(int(num)):
    print(str(util_functions.roll(1, 20)))

