import math, time
import classes.combat as c
import classes.encounters as e
import classes.hero as player
import classes.utility_functions as utils
dice = utils.Util()


print("Welcome, hero! What are you called?")
name = input(">> ")

hero = player.pick_class(name)

print() 

attr_dic = {"Name": hero.name, "Class": hero.class_name,
            "Level": hero.class_level, "HP": hero.health,
            "str": hero.str, "dex": hero.dex, "con": hero.con}

print()

for stat in attr_dic:
    print(stat + " : " + str(attr_dic[stat]))

input("[Enter]")
print()

hero.gold = 10
# begin dungeon crawl
encounters = ""
while hero.alive:
    # pick number of enemies
    num_combatants = dice.roll(1, math.ceil(hero.class_level/2))

    # pick random encounter (fight or shop or skill check)
    chance = dice.roll(1, 6)
    if chance > 1 or encounters == "shop":
        if encounters == "shop":  # skill check encounter
            encounters = "skill"
            e.skill_encounter(hero)

        elif chance in [2, 3, 4]:
            encounters = "fight"
            c.fight(hero, num_combatants)

        elif chance in [5, 6]:  # skill check encounter
            encounters = "skill"
            e.skill_encounter(hero)

    else:
        encounters = "shop"
        e.shop(hero)

    # heal between fights
    heal = math.floor(hero.max_health/2)
    if hero.health + heal >= hero.max_health:
        hero.health = hero.max_health
    else:
        hero.health += heal
print("{0.name} died at level {0.class_level} with {0.xp} XP".format(hero))
print("Goodbye")
input("[Enter]")
