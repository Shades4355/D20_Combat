import math
import classes.combat as c
import classes.encounters as e
import classes.hero as player
import classes.utility_functions as utils
dice = utils.Util()
pc = player.Pick_Class()


print("Welcome, hero! What are you called?")
name = input('>> ')

hero = pc.pick_class(name)

# begin dungeon crawl
while hero.alive:
    # pick number of enemies
    num_combatants = dice.roll(1, math.ceil(hero.class_level/2))

    # pick random encounter (fight or shop)
    enemies_in_fight = e.random_encounter(num_combatants, hero)
    while len(enemies_in_fight) > 0 and hero.alive:
        c.player_turn(hero, enemies_in_fight)
        c.enemy_turn(hero, enemies_in_fight)

    # heal between fights
    heal = math.floor(hero.max_health/2)
    if hero.health + heal >= hero.max_health:
        hero.health = hero.max_health
    else:
        hero.health += heal
print("{0.name} died at level {0.class_level}".format(hero))
print("Goodbye")
