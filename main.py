import classes.player as player

print("Welcome, hero! What are you called?")
name = input('>> ')

print("\nNext, pick a class:")
class_list = ["Fighter", "Rogue", "Wizard"]

util = player.Util()
class_name = util.pick_class()

player = player.Hero(name=name, class_name=class_name)
