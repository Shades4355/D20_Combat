import math, random
from classes import dice


def back_stab(player: object, enemy: object):
    attack_roll = dice.roll(1, 20) + player.stat_mod(player.dex)

    if attack_roll >= enemy.ac:
        print("{0.name} didn't see that coming!".format(enemy))
        enemy.take_damage(player.do_damage(True, player.stat_mod(player.dex)))
    else:
        print("{0.name} saw {1.name} coming and dodged".format(enemy, player))

def cleave(player: object, enemy: object, enemies_in_fight: list):
    """target up to 3 enemies"""
    targets = []

    # if 3 or fewer foes, attack all foes
    if len(enemies_in_fight) < 4:
        targets = enemies_in_fight
    else:
        enemy_index = enemies_in_fight.index(enemy)

        # first target
        enemy1 = None
        if enemy_index - 1 >= 0:
            enemy1 = enemies_in_fight[enemy_index - 1]
        else:
            enemy1 = enemies_in_fight[-1]

        # second target
        enemy2 = enemy

        # third target
        enemy3 = None
        if enemy_index + 1 <= len(enemies_in_fight) - 1:
            enemy3 = enemies_in_fight[enemy_index + 1]
        else:
            enemy3 = enemies_in_fight[0]

        targets = [enemy1, enemy2, enemy3]

    # attack the enemies
    for target in targets:
        roll = dice.roll(1, 20)
        attack_roll = roll + player.stat_mod(player.str)
        if roll == 20:
            target.take_damage(player.do_damage(True, player.stat_mod(player.str)))
        elif attack_roll > target.ac:
            target.take_damage(player.do_damage(
                False, player.stat_mod(player.str)))
        else:
            print(player.name, "missed", target.name)

def double_strike(player: object, enemy: object,
                  enemies_in_fight: list):
    player.attack(enemy, enemies_in_fight)
    if enemy.alive:
        player.attack(enemy, enemies_in_fight)
    else:
        print("{0.name} punched the corpse of {1.name}".format(player, enemy))

def fireball(player: object, enemies_in_fight: list):
    # attack the enemies
    for target in enemies_in_fight:
        roll = dice.roll(1, 20)
        if roll == 20:
            target.take_damage(player.do_damage(
                True, player.stat_mod(player.int), "magic"))
        else:
            target.take_damage(player.do_damage(
                False, player.stat_mod(player.int), "magic"))

def flurry(player: object, enemies_in_fight: list):
    num_of_attacks = math.floor(player.class_level / 3) + 3
    for i in range(num_of_attacks):
        enemy = random.choice(enemies_in_fight)
        if enemy.alive:
            roll = dice.roll(1, 20)
            attack = roll + player.stat_mod(player.dex)
            if roll == 20:
                print("Critical!")
                damage = player.do_damage(True, player.stat_mod(player.dex), "bludgeoning")
                enemy.take_damage(damage)
            elif attack >= enemy.ac:
                damage = player.do_damage(False, player.stat_mod(player.dex), "bludgeoning")
                enemy.take_damage(damage)
            else:
                print(player.name, "missed", enemy.name)
        else:
            print("{0.name} punched the corpse of {1.name}".format(player, enemy))

def magic_missile(player: object, enemy: object):
    num_of_missiles = math.floor(player.class_level/4) + 1
    damage = dice.roll(num_of_missiles, 4) + num_of_missiles
    enemy.take_damage(damage, False, "magic")
