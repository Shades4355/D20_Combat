import math
import classes.combat as c
import classes.encounters as e
import classes.hero as player
import classes.utility_functions as utils
dice = utils.Util()
pc = player.Pick_Class()

print("Welcome, hero! What are you called?")
name = input(">> ")

hero = pc.pick_class(name)

print() 

attr_dic = {"Name": hero.name, "Class": hero.class_name,
            "Level": hero.class_level, "HP": hero.health,
            "str": hero.str, "dex": hero.dex, "con": hero.con}

print()

for stat in attr_dic:
    print(stat + " : " + str(attr_dic[stat]))

input("[Enter]")
print()

# # hero.gain_xp(25)

# # print()

# # attr_dic2 = {"Name": hero.name, "Class": hero.class_name,
# #             "Level": hero.class_level, "HP": hero.health,
# #             "str": hero.str, "dex": hero.dex, "con": hero.con}

# # for stat in attr_dic2:
# #     print(stat + " : " + str(attr_dic2[stat]))

# # input("[Enter]")
# # print()

# # fighter = heros.Fighter(name="Fighter")

# # fighter_attr_dic = {"Name": fighter.name, "Class": fighter.class_name,
# #             "Level": fighter.class_level, "HP": fighter.health,
# #             "str": fighter.str, "dex": fighter.dex, "con": fighter.con}

# # print()

# # for stat in fighter_attr_dic:
# #     print(stat + " : " + str(fighter_attr_dic[stat]))


# # input("[Enter]")
# # print()


# begin dungeon crawl
while hero.alive:
    # pick number of enemies
    num_combatants = dice.roll(1, math.ceil(hero.class_level/2))

    # pick random encounter (fight or shop)
    if dice.roll(1, 3) > 1:
        enemies_in_fight = e.random_encounter(num_combatants, hero)
        while len(enemies_in_fight) > 0 and hero.alive:
            c.player_turn(hero, enemies_in_fight)
            c.enemy_turn(hero, enemies_in_fight)
    else:
        e.shop(hero)

    # heal between fights
    heal = math.floor(hero.max_health/2)
    if hero.health + heal >= hero.max_health:
        hero.health = hero.max_health
    else:
        hero.health += heal
print("{0.name} died at level {0.class_level} with {0.xp} XP".format(hero))
print("Goodbye")