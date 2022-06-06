import classes.utility_functions as util
import classes.hero as heros

util = util.Util()

print("Welcome, hero! What are you called?")
name = input(">> ")

hero = util.pick_class(name)

print() 

attr_dic = {"Name": hero.name, "Class": hero.class_name,
            "Level": hero.class_level, "HP": hero.health,
            "str": hero.str, "dex": hero.dex, "con": hero.con}

print()

for stat in attr_dic:
    print(stat + " : " + str(attr_dic[stat]))

input("[Enter]")
print()

# hero.gain_xp(25)

# print()

# attr_dic2 = {"Name": hero.name, "Class": hero.class_name,
#             "Level": hero.class_level, "HP": hero.health,
#             "str": hero.str, "dex": hero.dex, "con": hero.con}

# for stat in attr_dic2:
#     print(stat + " : " + str(attr_dic2[stat]))

# input("[Enter]")
# print()

fighter = heros.Fighter(name="Fighter")

fighter_attr_dic = {"Name": fighter.name, "Class": fighter.class_name,
            "Level": fighter.class_level, "HP": fighter.health,
            "str": fighter.str, "dex": fighter.dex, "con": fighter.con}

print()

for stat in fighter_attr_dic:
    print(stat + " : " + str(fighter_attr_dic[stat]))

input("[Enter]")
print()

print("How many time would you like to roll 1d20?")
num = input(">> ")
print("Rolling 1d20 " + str(num) + " times: ")
for i in range(int(num)):
    print(str(util.roll(1, 20)))

