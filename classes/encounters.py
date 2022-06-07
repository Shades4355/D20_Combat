import random


def random_encounter(num_combatants: int, player: object):
    encounters = []

    if player.level <= 3:
        encounters = [shop, goblin_encounter, wolf_encounter]
    elif player.level <= 6:
        encounters = [shop, goblin_encounter, wolf_encounter,
                      undead_encounter, zombie_encounter]
    else:
        encounters = [shop, goblin_encounter, wolf_encounter,
                      undead_encounter, zombie_encounter, vampire_encounter]

    randomChoice = random.choices(encounters)[0]

    return randomChoice(num_combatants)


def shop(num_of_foes: int):
    pass


def goblin_encounter(num_of_foes: int):
    pass


def wolf_encounter(num_of_foes: int):
    pass


def undead_encounter(num_of_foes: int):
    pass


def zombie_encounter(num_of_foes: int):
    pass


def vampire_encounter(num_of_foes: int):
    pass
