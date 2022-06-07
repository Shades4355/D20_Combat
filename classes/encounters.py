import random


def random_encounter(num_combatants: int, player: object):
    encounters = []

    if player.level <= 3:
        encounters = [shop, goblinEncounter, wolfEncounter]
    elif player.level <= 6:
        encounters = [shop, goblinEncounter, wolfEncounter,
                      undeadEncounter, zombieHorde]
    else:
        encounters = [shop, goblinEncounter, wolfEncounter,
                      undeadEncounter, zombieHorde, vampireEncounter]

    randomChoice = random.choices(encounters)[0]

    return randomChoice(num_combatants)


