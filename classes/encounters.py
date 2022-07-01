import random, time, math, sys
from classes import enemies as e
from classes import combat as c
from classes import dice
from equipment import weapons as w
from equipment import armor as a
import save_load as s



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

        {"name": "{0.name} (+{0.value})".format(a.Leather()),
         "type": "armor",
         "armor": a.Leather(),
         "price": a.Leather().price},
        {"name": "{0.name} (+{0.value})".format(a.Hide()),
         "type": "armor",
         "armor": a.Hide(),
         "price": a.Hide().price},
        {"name": "{0.name} (+{0.value})".format(a.Chain()),
         "type": "armor",
         "armor": a.Chain(),
         "price": a.Chain().price},
        {"name": "{0.name} (+{0.value})".format(a.Scale()),
         "type": "armor",
         "armor": a.Scale(),
         "price": a.Scale().price},
        {"name": "{0.name} (+{0.value})".format(a.HalfPlate()),
         "type": "armor",
         "armor": a.HalfPlate(),
         "price": a.HalfPlate().price},
        {"name": "{0.name} (+{0.value})".format(a.FullPlate()),
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
         "equip": w.HandAxe()},
         {"name": w.Rod().name,
          "type": "weapon",
          "price": 10,
          "equip": w.Rod()}
    ]

    back = {
        "name": "back",
        "type": "back",
        "price": 0
    }

    # save?
    print("Save progress?")
    choice = ""
    while choice.lower() not in ["yes", "no"]:
        print('"Yes" / "No"')
        choice = input(">> ")
    if choice.lower() == "yes":
        s.save(player)

    # heal after combat
    print("\nEntering the clearing, you see a safe place to rest, and a traveling merchant")
    heal = math.floor(player.max_health/4)

    if player.health + heal > player.max_health:
        heal = player.max_health - player.health

    player.health += heal
    print("You recover {} HP, bringing you to {} HP".format(heal, player.health))
    print()
    time.sleep(1)
    
    # reset cooldown on entering shop
    player.cooldown = 0

    # pick items for sale
    forSaleList = random.choices(items, k=3 + player.stat_mod(player.wis))
    forSaleList.append(back)

    # choose an item to buy; or leave
    inShop = True
    while inShop == True:
        choice = ''
        while choice not in [i["name"] for i in forSaleList]:
            print()
            print("Player gold: " + str(player.gold))
            print("Equipped Weapon: {}".format(player.weapon.name))
            print("Worn Armor: {0.name} (+{0.value})".format(player.armor))
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


def skill_encounter(player: object):
    encounters = [listen_check, mysterious_mushroom, rubble_encounter, boxing_encounter]

    random_encounter = random.choices(encounters)[0]
    return random_encounter(player)


def listen_check(player: object):
    dc = 15
    print("\nYour senses tingle; did you just hear something?")
    roll = dice.roll(1, 20) + player.stat_mod(player.wis)
    time.sleep(1)
    print("\nPerception check:", roll)
    time.sleep(1)

    if roll >= dc: # success
        print("\nYou hear a fight ahead. Do you wait for the victory to leave, or attack them while they're weak?")

        choice = ""
        while choice.lower() not in ["wait", "attack"]:
            print('"wait" or "attack"?')
            choice = input(">> ")
        print()
        if choice.lower() == "attack":
            print("You wait for the sounds of combat to cease, and then you attack!")
            num_of_enemies = dice.roll(1, math.ceil(player.class_level/4))
            c.fight(player, num_of_enemies)
        
        elif choice.lower() == "wait":
            print("You wait for the sounds of combat to cease, and then a minute more")
            print("You round the corner to see the carnage of battle")
            print("Let's see if there's any loot left behind!")
            time.sleep(1)
            c.equipment_drop(player, nothing=1, armor=2, weapon=2, gold=4)
    
    else: # failure
        print("\nIt's probably just your imagination...")
        print("You round the corner to find yourself in the middle of a fight!")
        num_of_enemies = dice.roll(1, player.class_level)
        c.fight(player, num_of_enemies)


def mysterious_mushroom(player: object):
    def eat_mushroom(player: object, luck: int):
        if luck == 1:
            print("You eat the mushroom...")
            time.sleep(1)
            print("Delicious!")
            time.sleep(1)
            xp = dice.roll(1, 4)
            print()
            print("You gained {} XP".format(xp))
            player.gain_xp(xp)
            time.sleep(1)
            print()
        else:
            print("You eat the mushroom...")
            time.sleep(1)
            print("Your stomach doesn't feel so good...")
            time.sleep(1)
            print()
            damage = dice.roll(1, 6)
            player.take_damage(damage)
            time.sleep(1)
            print()

    luck = dice.roll(1,2) # 1 = good; 2 = bad
    dc = 15
    roll = dice.roll(1,20) + player.stat_mod(player.int)

    print("\nYou come across a mysterious mushroom")
    print("Looks tasty...")
    time.sleep(1)
    print("\nIdentify the mushroom, eat it, or leave it?")
    choice = ""

    options = ["identify", "eat", "leave it"]
    while choice.lower() not in options:
        print('"identify", "eat", or "leave it"?')
        choice = input(">> ")
    
    print()
    if choice.lower() == "eat":
        eat_mushroom(player, luck)
    elif choice.lower() == "identify":
        print("Knowledge Nature:", roll)
        time.sleep(1)
        print()
        if roll >= dc:
            if luck == 1: # good option
                print("Seems safe")
                time.sleep(1)
                eat_mushroom(player, luck)
            else: # bad mushroom
                print("This mushroom is no good!")
                time.sleep(1)
                print("You throw the mushroom away")
        else:
            print("Better not to risk it")
            time.sleep(1)
            print()
    elif choice.lower() == "leave it":
        print("You leave the mushroom unpicked and continue on")
        time.sleep(1)
        print()
    else:
        print("Mushroom Error!")
        sys.exit(1)


def boxing_encounter(player: object):
    dc = 12
    print("You are cordially invited to participate in a boxing competition.")
    print("The winner will be awarded an amount of gold")
    
    choice = ""
    while choice.lower() not in ["compete", "pass"]:
        print('"Compete" or "pass"?')
        choice = input(">> ")
    
    if choice.lower() == "compete":
        roll = dice.roll(1,20) + player.stat_mod(player.con)
        print("\nCon check:", roll)
        time.sleep(1)
        print()

        if roll >= dc:
            print("You win!")
            time.sleep(1)
            reward = dice.roll(2,4)
            print("You win {} gold!".format(reward))
            player.gold += reward
            time.sleep(1)
            print()
        else:
            print("You take a beating and go down in the third round")
            damage = 0
            for i in range(player.class_level):
                damage += dice.roll(2,4)
            player.take_damage(damage)
            time.sleep(1)
            print()
    else:
        print("Best not to risk this pretty face")
        time.sleep(1)
        print()


def rubble_encounter(player):
    dc = 17

    print("\nBefore you a wall of fallen rubble blocks your path")
    print("Will you dig your way through, climb over, or turn around?")

    choice = ""
    while choice.lower() not in ["dig", "climb", "leave"]:
        print('"dig", "climb", "leave"')
        choice = input(">> ")
        print()

    if choice.lower() == "dig":
        print("You start digging through the rubble...")
        time.sleep(1)
        roll = dice.roll(1, 20) + player.stat_mod(player.str)
        print("Strength:", roll)
        time.sleep(1)
        print()
        if roll >= dc: # success
            print("You finish digging your way through, and see a shop ahead")
            time.sleep(1)
            xp = dice.roll(1, 4)
            print("You gain {} XP".format(xp))
            player.gain_xp(xp)
            time.sleep(2)
            shop(player)
        else: # fail
            print("You dig until your hands hurt...")
            print()
            damage = dice.roll(player.class_level, 4)
            player.take_damage(damage)
            time.sleep(1)
            print()
            print("But you've made almost no progress.")
            print("It's time to call it quits and find another route")
            time.sleep(2)
    elif choice.lower() == "climb":
        print("You begin climbing the rubble")
        print("The rubble starts shifting under your feet")
        time.sleep(1)
        roll = dice.roll(1,20) + player.stat_mod(player.dex)
        print("Dexterity:", roll)
        time.sleep(1)
        print()
        if roll >= dc: # success
            print("But your surefootedness carries you through!")
            time.sleep(1)
            print("On the other side you see a shop!")
            time.sleep(1)
            xp = dice.roll(1, 4)
            print("You gain {} XP".format(xp))
            player.gain_xp(xp)
            time.sleep(2)
            shop(player)
        else: # fail
            print("The rubble goes out from under you and you fall")
            print()
            damage = dice.roll(player.class_level, 4)
            player.take_damage(damage)
            time.sleep(1)
            print()
            print("You decide not to try that again,")
            print("and instead look for another route")
            time.sleep(2)
    elif choice.lower() == "leave":
        print("You turn around and leave")
        time.sleep(2)


def random_encounter(num_combatants: int, player: object):
    encounters = []

    if player.class_level <= 3:
        encounters = [goblin_encounter, goblin_horde_encounter]
    elif player.class_level <= 6:
        encounters = [goblin_encounter, goblin_horde_encounter, 
                      wolf_encounter, undead_encounter, zombie_encounter]
    else:
        encounters = [goblin_encounter, wolf_encounter,
                      undead_encounter, zombie_horde_encounter, vampire_horde]

    # pick encounter
    randomChoice = random.choices(encounters)[0]

    return randomChoice(num_combatants)


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


def vampire_horde(num_of_foes: int):
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
