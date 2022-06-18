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


hero.gold = 25
e.shop(hero)

# begin dungeon crawl
while hero.alive:
    # pick number of enemies
    num_combatants = dice.roll(1, math.ceil(hero.class_level/2))

    # pick random encounter (fight or shop)
    if dice.roll(1, 4) > 1:
        enemies_in_fight = e.random_encounter(num_combatants, hero)
        hero.in_fight = True
        
        #print player health and level
        time.sleep(1)
        print("\n### New Encounter ###")
        print("\n{0.name}\nHealth: {0.health}\nLevel: {0.class_level}".format(hero))
        time.sleep(1)

        while hero.in_fight and hero.alive:
            c.player_turn(hero, enemies_in_fight)
            if hero.cooldown > 0:
                hero.cooldown -= 1
            c.enemy_turn(hero, enemies_in_fight)
            if len(enemies_in_fight) <= 0:
              hero.in_fight = False
    else:
        e.shop(hero)
        hero.cooldown = 0

    # heal between fights
    heal = math.floor(hero.max_health/2)
    if hero.health + heal >= hero.max_health:
        hero.health = hero.max_health
    else:
        hero.health += heal
print("{0.name} died at level {0.class_level} with {0.xp} XP".format(hero))
print("Goodbye")
