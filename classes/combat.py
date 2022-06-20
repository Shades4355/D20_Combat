import sys, random
from equipment import weapons as w
from equipment import armor as a
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
    #  special #   back    #
    ######### quit #########
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
        elif choice.lower() == "attack":
            player.attack(enemy, enemies_in_fight)
            break
        elif choice.lower() == "back":
            player_turn(player, enemies_in_fight)
            break
        elif choice == "quit":
            print("Goodbye")
            print("{0.name} reached level {0.class_level} with {0.xp} XP".format(player))
            input("[Enter]")
            sys.exit(0)

    # Checks if enemies are dead
    for i in range(len(enemies_in_fight) - 1, -1, -1):
        target = enemies_in_fight[i]
        if not target.alive:
            player.gain_xp(target.grantXP)
            player.gold += target.loot
            del enemies_in_fight[i]
            equipment_drop(player)

def equipment_drop(player: object):
    # drop nothing: 3 weight
    nothing_table = [
        {"name": "nothing",
        "type": "nothing",
        "equip": None}]
    
    # drop weapon:  1 weight
    weapon_table = [
        {"name": w.Unarmed().name,
        "type": "weapon",
        "equip": w.Unarmed()},
        {"name":w.HandAxe().name,
        "type": "weapon",
        "equip": w.HandAxe()},
        {"name": w.ShortSword().name,
        "type": "weapon",
        "equip": w.ShortSword()},
        {"name": w.LongSword().name,
        "type": "weapon",
        "equip": w.LongSword()},
        {"name": w.Poleaxe().name,
        "type": "weapon",
        "equip": w.Poleaxe()},
        {"name": w.Staff().name,
        "type": "weapon",
        "equip": w.Staff()}]

    # drop armor:   1 weight
    armor_table = [
        {"name": a.Leather().name,
         "type": "armor",
         "equip": a.Leather()},
         {"name": a.Hide().name,
         "type": "armor",
         "equip": a.Hide()},
         {"name": a.Chain().name,
         "type": "armor",
         "equip": a.Chain()},
         {"name": a.Scale().name,
         "type": "armor",
         "equip": a.Scale()},
         {"name": a.HalfPlate().name,
          "type": "armor",
          "equip": a.HalfPlate()},
        {"name": a.FullPlate().name,
         "type": "armor",
         "equip": a.FullPlate()}]

    # drop gold:    3 weight
    gold_drop = [
        {"name": "gold",
         "type": "gold",
         "equip": dice.roll(1, 3)},
        {"name": "gold",
        "type": "gold",
        "equip": dice.roll(1,4)},
        {"name": "gold",
         "type": "gold",
         "equip": dice.roll(1, 6)}]

    drop_table = random.choice([nothing_table, weapon_table, armor_table, gold_drop], 3, 1, 1, 3, k=1)

    drop = random.choice(drop_table, k=1)

    print("Monster drop: {}".format(drop["name"]))
    
    if drop["type"] != "nothing":
        print("take or pass?")
        choice = ""
        while choice.lower() not in ["take", "pass"]:
            choice = input(">> ")
        
        if choice.lower() == "take":
            # equip weapon
            # equip armor
            # acquire gold
            pass
