import sys
import classes.utility_functions as utils
dice = utils.Util()

def enemy_turn(player:object, enemies_in_fight:list):
    for enemy in enemies_in_fight:
        roll = dice.roll(1, 20)
        attack_roll = roll + enemy.str_mod + enemy.attack_bonus

        if roll == 20:
            damage = enemy.do_damage(True)
        elif attack_roll > player.ac:
            damage = enemy.do_damage(False)
            player.take_damage(damage)
        else:
            print(enemy.name, "missed")

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
            pass
        elif "special" in choice.lower():
            # show special moves
            pass
        elif choice == "attack":
            player.attack(enemy, enemies_in_fight)
            break
        elif choice == "quit":
            print("Goodbye")
            print("{0.name} reached level {0.level}".format(player))
            sys.exit()

