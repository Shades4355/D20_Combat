import classes.player as player

print("Welcome, hero! What are you called?")
name = input('>> ')

print("\nNext, pick a class:")
class_list = ["Fighter", "Rogue", "Wizard"]

class_name = "Null"
while class_name not in class_list:
    print(", ".join(class_list))
    class_name = input(">> ")
    class_name = class_name.capitalize()




player = player.Hero(name=name, class_name=class_name)
