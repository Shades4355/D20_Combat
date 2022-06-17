import random, time
import classes.enemies as e
from equipment import weapons as w
from equipment import armor as a
import classes.utility_functions as utils
dice = utils.Util()


def random_encounter(num_combatants: int, player: object):
    encounters = []

    if player.class_level <= 3:
        encounters = [goblin_encounter, goblin_horde_encounter]
    elif player.class_level <= 6:
        encounters = [goblin_encounter, goblin_horde_encounter, 
                      wolf_encounter, undead_encounter, zombie_encounter]
    else:
        encounters = [goblin_encounter, wolf_encounter,
                      undead_encounter, zombie_horde_encounter, vampire_encounter]

    randomChoice = random.choices(encounters)[0]

    return randomChoice(num_combatants)


def shop(player: object):    
    items = [
        {"name": "cure light potion",
         "type": "item",
         "price": 2},
        {"name": "cure moderate potion",
         "type": "item",
         "price": 4},
         {"name": "cure serious potion",
         "type": "item",
         "price": 8},
        {"name": "scroll of escape",
         "type": "item",
         "price": 2},

        {"name": a.Leather().name,
         "type": "armor",
         "armor": a.Leather(),
         "price": a.Leather().price},
        {"name": a.Hide().name,
         "type": "armor",
         "armor": a.Hide(),
         "price": a.Hide().price},
        {"name": a.Chain().name,
         "type": "armor",
         "armor": a.Chain(),
         "price": a.Chain().price},
        {"name": a.Scale().name,
         "type": "armor",
         "armor": a.Scale(),
         "price": a.Scale().price},
        {"name": a.HalfPlate().name,
         "type": "armor",
         "armor": a.HalfPlate(),
         "price": a.HalfPlate().price},
        {"name": a.FullPlate().name,
         "type": "armor",
         "armor": a.FullPlate(),
         "price": a.FullPlate().price},

        {"name": w.LongSword().name,
         "type": "weapon",
         "price": 3,
         "equip": w.LongSword()},
        {"name": w.ShortSword().name,
         "type": "weapon",
         "price": 3,
         "equip": w.ShortSword()},
        {"name": w.Unarmed().name,
         "type": "weapon",
         "price": 0,
         "equip": w.Unarmed()},
        {"name": w.Staff().name,
         "type": "weapon",
         "price": 10,
         "equip": w.Staff()},
        {"name": w.Poleaxe().name,
         "type": "weapon",
         "price": 5,
         "equip": w.Poleaxe()},
        {"name": w.HandAxe().name,
        "type": "weapon",
        "price": 3,
         "equip": w.HandAxe()}
    ]

    back = {
        "name": "back",
        "type": "back",
        "price": 0
    }

    # pick items for sale
    forSaleList = random.choices(items, k= 3 + player.stat_mod(player.wis))
    forSaleList.append(back)

    # choose an item to buy; or leave
    inShop = True
    while inShop == True:
        choice = ''
        while choice not in [i["name"] for i in forSaleList]:
            print()
            print("Player gold: " + str(player.gold))
            print("Equipped Weapon: {}".format(player.weapon.name))
            print("Worn Armor: {}".format(player.armor.name))
            print()
            time.sleep(1)
            
            for item in forSaleList:
                if item["name"] != "back":
                    price = item["price"] - player.stat_mod(player.cha)
                    if price <= 1:
                        price = 1
                else:
                    price = item["price"]

                item["price"] = price

                print(item["name"] + "\n\tPrice: " + str(price))
            choice = input("What would you like to buy?\n>> ")

        index = [i["name"] for i in forSaleList].index(choice)
        choice = forSaleList[index]

        if choice["name"] == "back":  # leave shop
            inShop = False
        elif player.gold >= choice["price"]:
            player.gold -= choice["price"]
            if choice["type"] == "item":
                player.inventory.append(choice["name"])
            elif choice["type"] == "armor":
                player.armor = choice["armor"]
                player.update_ac()
            elif choice["type"] == "weapon":
                player.weapon = choice["equip"]
            forSaleList.remove(choice)
        else:
            print("You can't afford that.\n")
            choice = ''
        player.check_inventory()


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


def goblin_horde_encounter(num_of_foes: int):
    g = 0

    encounter = []

    for i in range(num_of_foes * 2):
        g += 1
        encounter.append(e.Goblin(name="Goblin {}".format(g)))
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
    return encounter
    

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
    return encounter
