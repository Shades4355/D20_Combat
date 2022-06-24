import math, time
import classes.combat as c
import classes.encounters as e
import classes.hero as player
import classes.utility_functions as utils
dice = utils.Util()


print("Welcome, hero! What are you called?")
name = input('>> ')

hero = player.pick_class(name)

hero.gold = 10
# begin dungeon crawl
encounters = ""
while hero.alive:
    # pick number of enemies
    num_combatants = dice.roll(1, math.ceil(hero.class_level/2))

    # pick random encounter (fight or shop)
    chance = dice.roll(1, 6)
    print("Chance roll:", chance) # TODO: remove
    if chance > 1 or encounters == "shop":
        if encounters == "shop":
            # skill check encounter
            # TODO: implement skill encounters
            encounters = "skill"
            print("skipping shop encounter") # TODO: remove
            pass
        elif chance in [2, 3, 4]:
            enemies_in_fight = e.random_encounter(num_combatants, hero)
            encounters = "fight"
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
        elif chance in [5, 6]: # skill check encounter
            # TODO: implement skill encounters
            print("skipping skill encounter") # TODO: remove
            encounters = "skill"
            pass
    else:
        e.shop(hero)
        encounters = "shop"
        hero.cooldown = 0
    
    # heal between fights
    heal = math.floor(hero.max_health/2)
    if hero.health + heal >= hero.max_health:
        hero.health = hero.max_health
    else:
        hero.health += heal
print("{0.name} died at level {0.class_level} with {0.xp} XP".format(hero))
print("Goodbye")
input("[Enter]")
