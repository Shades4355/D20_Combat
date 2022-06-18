import sys
import classes.utility_functions as utils
dice = utils.Util()

def enemy_turn(player:object, enemies_in_fight:list):
    for enemy in enemies_in_fight:
        enemy.attack(player)

def player_turn(player:object, enemies_in_fight:list):
    _COMBAT_ACTIONS = ["attack", "inventory", "special", "quit"]

    MAIN_COMBAT_DISPLAY_PIC = '''
    ########################
    #  attack  # inventory #
    #  special #   quit    #
    ########################
    '''
    
    print("\nPick Target:")
    for i in range(len(enemies_in_fight)):
        print(str(i + 1) + ": " + enemies_in_fight[i].name)

    # targeting #
    target = 0
    while target - 1 not in range(len(enemies_in_fight)):
      target = input(">> ")
      try:
          target = int(target)
      except:
          target = 0

    enemy = enemies_in_fight[target - 1]

    print("Enemy has {} hit points and {} lives".format(
        enemy.current_hit_points, enemy.lives))

    # action choice #
    choice = None
    while choice not in _COMBAT_ACTIONS:
        print(MAIN_COMBAT_DISPLAY_PIC)
        choice = input(">> ").lower()

        if "inventory" in choice.lower():
            # show inventory
            player.show_inventory(player_turn, enemies_in_fight)
        elif "special" in choice.lower():
            # show special moves
            player.show_specials(enemy, enemies_in_fight, player_turn)
        elif choice == "attack":
            player.attack(enemy, enemies_in_fight)
            break
        elif choice == "quit":
            print("Goodbye")
            print("{0.name} reached level {0.class_level}".format(player))
            sys.exit()

    # Checks if enemies are dead
    for i in range(len(enemies_in_fight) - 1, -1, -1):
        enemy = enemies_in_fight[i]
        if not enemy.alive:
            player.gain_xp(enemy.grantXP)
            player.gold += enemy.loot
            del enemies_in_fight[i]
            equipment_drop(player)

def equipment_drop(player: object):
    pass
