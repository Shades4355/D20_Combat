import math
import classes.combat as c
import classes.encounters as e
import classes.utility_functions as utils
util = utils.Util()


print("Welcome, hero! What are you called?")
name = input('>> ')

player = util.pick_class(name)

# begin dungeon crawl
while player.alive:
    # pick number of enemies
    num_combatants = util.roll(1, math.ceil(player.level/2))
    
    # pick random encounter (fight or shop)
    enemies_in_fight = e.random_encounter(num_combatants, player)
    while len(enemies_in_fight) > 0:
        c.player_turn(player, enemies_in_fight)
        c.enemy_turn(player, enemies_in_fight)
    
    # heal between fights
    heal = math.floor(player.max_health/2)
    if player.health + heal >= player.max_health:
        player.health = player.max_health
    else:
        player.health += heal
    
