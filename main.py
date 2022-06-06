import classes.utility_functions as util

print("Welcome, hero! What are you called?")
name = input('>> ')

util = util.Util()
player = util.pick_class(name)
