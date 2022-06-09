import random
import classes.enemies as e
import classes.utility_functions as utils
dice = utils.Util()


def random_encounter(num_combatants: int, player: object):
    encounters = []

    if player.level <= 3:
        encounters = [goblin_encounter, wolf_encounter]
    elif player.level <= 6:
        encounters = [goblin_encounter, wolf_encounter,
                      undead_encounter, zombie_encounter]
    else:
        encounters = [goblin_encounter, wolf_encounter,
                      undead_encounter, zombie_encounter, vampire_encounter]

    randomChoice = random.choices(encounters)[0]

    return randomChoice(num_combatants)


def shop(num_of_foes: int):
    pass


def goblin_encounter(num_of_foes: int):
    """A table for random goblin encounter
    
    includes goblins, hobgoblins, and wolves"""
    encounter = []
    g = 0
    h = 0
    w = 0

    for i in range (num_of_foes):
        rand_num = dice.roll(1, 3)

        if rand_num == 1:
            g += 1
            encounter.append(e.Goblin(name="Goblin {}".format(g)))
        elif rand_num == 2:
            h += 1
            encounter.append(e.Hobgoblin(name="Hobgoblin {}".format(h)))
        elif rand_num == 3:
            w += 1
            encounter.append(e.Wolf(name="Wolf {}".format(w)))
    
    return encounter


def wolf_encounter(num_of_foes: int):
    """A table for random wolf encounters
    
    includes regular wolves and dire wolves"""
    encounter = []
    w = 0
    d = 0
    rand_num = dice.roll(1, 3)

    for i in range(num_of_foes):
        if rand_num == 2 or rand_num == 3:
            w += 1
            encounter.append(e.Wolf(name="Wolf {}".format(w)))
        else:
            d += 1
            encounter.append(e.DireWolf(name="Dire Wolf {}".format(d)))

    return encounter


def undead_encounter(num_of_foes: int):
    """a table for a random undead encounter
    
    includes zombies, skeletons, and ghouls"""
    encounter = []
    z = 0
    s = 0
    g = 0

    for i in range(num_of_foes):
        rand_num = dice.roll(1, 3)

        if rand_num == 1:
            z += 1
            encounter.append(e.Zombie(name="Zombie {}".format(z)))
        elif rand_num == 2:
            s += 1
            encounter.append(e.Skeleton(name="Skeleton {}".format(s)))
        else:
            g += 1
            encounter.append(e.Ghoul(name="Ghoul {}".format(g)))
    
    return encounter


def zombie_encounter(num_of_foes: int):
    """a table for random zombie encounters
    
    includes only zombies"""
    encounter = []
    z = 0

    for i in range(num_of_foes):
        z += 1
        encounter.append(e.Zombie(name="Zombie {}".format(z)))


def zombie_horde_encounter(num_of_foes: int):
    return zombie_encounter(num_of_foes * 2)


def vampire_encounter(num_of_foes: int):
    """a table for a random vampire encounter
    
    includes vampires and a vampire lord"""
    encounter = []
    v = 0
    l = 0

    for i in range(num_of_foes):
        if l < 1:
            rand_num = dice.roll(1, 2)
            if rand_num == 1:
                l += 1
                encounter.append(e.VampireLord(name="Vampire Lord"))
            else:
                v += 1
                encounter.append(e.Vampire(name="Vampire {}".format(v)))
        else:
            v += 1
            encounter.append(e.Vampire(name="Vampire {}".format(v)))
