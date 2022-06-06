import classes.utility_functions as util

print("Welcome, hero! What are you called?")
name = input('>> ')

util = util.Util()
player = util.pick_class(name)

# begin dungeon crawl
# while loop
play_game = True
while play_game == True:
    # pick random encounter (fight or shop)
    # pick number of enemies
    # fight
    while player.health > 0:
        pass
    # recover
    pass