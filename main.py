import math, time
from classes import combat as c
from classes import encounters as e
from classes import hero as player
from classes import dice
import save_load as s


# Load, or New Game?
encounters = ""
choice = ''
while choice.lower() not in ['new game', 'load']:
    print("'New Game' or 'Load'?")
    choice = input(">> ")
print()

if choice.lower() == "load":
    try:
        hero = s.load()
        print("Welcome back,", hero.name)
        time.sleep(1)
        print()
        encounters = "shop"
        e.shop(hero)
    except:
        print("I'm sorry, save file can't be found")
        print("Welcome, hero! What are you called?")
        name = input('>> ')

        hero = player.pick_class(name)
        time.sleep(1)
        print()
        hero.gold = 10
else:
    print("Welcome, hero! What are you called?")
    name = input('>> ')

    hero = player.pick_class(name)
    time.sleep(1)
    print()
    hero.gold = 10

# begin dungeon crawl
while hero.alive:
    # pick number of enemies
    num_combatants = dice.roll(1, math.ceil(hero.class_level/2))

    # pick random encounter (fight or shop or skill check)
    chance = dice.roll(1, 6)
    if chance > 1 or encounters == "shop":
        if encounters == "shop" or chance in [5, 6]:  # skill check encounter
            encounters = "skill"
            e.skill_encounter(hero)

        elif chance in [2, 3, 4]:
            encounters = "fight"
            c.fight(hero, num_combatants)
    else:
        encounters = "shop"
        e.shop(hero)

print("\n{0.name} died at level {0.class_level} with {0.xp} XP".format(hero))
print("Goodbye")
input("[Enter]")
