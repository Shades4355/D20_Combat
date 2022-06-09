import math
import classes.utility_functions as utils

util = utils.Util()

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

# fighter = heros.Fighter(name="Fighter")

# fighter_attr_dic = {"Name": fighter.name, "Class": fighter.class_name,
#             "Level": fighter.class_level, "HP": fighter.health,
#             "str": fighter.str, "dex": fighter.dex, "con": fighter.con}

# print()

# for stat in fighter_attr_dic:
#     print(stat + " : " + str(fighter_attr_dic[stat]))

# input("[Enter]")
# print()

# print("How many time would you like to roll 1d20?")
# num = input(">> ")
# print("Rolling 1d20 " + str(num) + " times: ")
# for i in range(int(num)):
#     print(str(util.roll(1, 20)))


# begin dungeon crawl
while hero.alive:
    # pick number of enemies
    num_combatants = util.roll(1, math.ceil(hero.level/2))

    # pick random encounter (fight or shop)
    enemies_in_fight = e.random_encounter(num_combatants, hero)
    while len(enemies_in_fight) > 0:
        c.player_turn(hero, enemies_in_fight)
        c.enemy_turn(hero, enemies_in_fight)

    # heal between fights
    heal = math.floor(hero.max_health/2)
    if hero.health + heal >= hero.max_health:
        hero.health = hero.max_health
    else:
        hero.health += heal
