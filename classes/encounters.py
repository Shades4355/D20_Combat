import random, time, math, sys
from classes import enemies as e
from classes import combat as c
from classes import dice
from equipment import weapons as w
from equipment import armor as a
import save_load as s


def shop(player: object, save: bool =True):
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
        "name": "leave",
        "type": "back",
        "price": 0
    }

    if save == True:
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
        choice = None
        while choice not in [i["name"] for i in forSaleList] and choice not in range(1, len(forSaleList) + 1):
            print()
            print("Player gold: " + str(player.gold))
            print("Equipped Weapon: {}".format(player.weapon.name))
            print("Worn Armor: {0.name} (+{0.value})".format(player.armor))
            print()
            time.sleep(1)

            n=0
            for item in forSaleList:
                if item["name"] != "leave":
                    price = item["price"] - player.stat_mod(player.cha)
                    if price <= 1:
                        price = 1
                else:
                    price = item["price"]

                item["price"] = price

                n+=1
                print(str(n) + ": " + item["name"] + "\n\tPrice: " + str(price))
            
            choice = input("What would you like to buy?\n>> ")
            num = False
            try:
                choice = int(choice)
                num = True
            except:
                num = False

        indexed_choice = None
        if num == False:
            index = [i["name"] for i in forSaleList].index(choice)
            indexed_choice = forSaleList[index]
        elif num == True:
            indexed_choice = forSaleList[choice - 1]

        if indexed_choice["name"] == "leave":  # leave shop
            inShop = False
        elif player.gold >= indexed_choice["price"]:
            player.gold -= indexed_choice["price"]
            if indexed_choice["type"] == "item":
                player.inventory.append(indexed_choice["name"])
            elif indexed_choice["type"] == "armor":
                player.armor = indexed_choice["armor"]
                player.update_ac()
            elif indexed_choice["type"] == "weapon":
                player.weapon = indexed_choice["equip"]
            forSaleList.remove(indexed_choice)
        else:
            print("You can't afford that.\n")
            choice = ""
            indexed_choice = None
        player.check_inventory()
        time.sleep(1)
        print()


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
    print()

    if roll >= dc: # success
        print("You hear a fight ahead. Do you wait for the victory to leave, or attack them while they're weak?")

        choice = ""
        while choice.lower() not in ["wait", "attack"]:
            print('"wait" or "attack"?')
            choice = input(">> ")
        print()
        if choice.lower() == "attack":
            print("You wait for the sounds of combat to cease, and then you attack!")
            num_of_enemies = dice.roll(1, math.ceil(player.class_level/4))
            c.fight(player, num_of_enemies, False)
        
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
        c.fight(player, num_of_enemies, False)
    print()


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
        else:
            print("You eat the mushroom...")
            time.sleep(1)
            print("Your stomach doesn't feel so good...")
            time.sleep(1)
            print()
            damage = dice.roll(1, 6)
            player.take_damage(damage)
            time.sleep(1)

    luck = dice.roll(1,2) # 1 = good; 2 = bad
    dc = 15
    roll = dice.roll(1,20) + player.stat_mod(player.int)

    print("\nYou come across a mysterious mushroom")
    print("Looks tasty...")
    time.sleep(1)
    print()
    print("Identify the mushroom, eat it, or leave it?")
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
    elif choice.lower() == "leave it":
        print("You leave the mushroom unpicked and continue on")
        time.sleep(1)
    else:
        print("Mushroom Error!")
        sys.exit(1)
    print()


def boxing_encounter(player: object):
    dc = 12
    multiplier = 3
    print("You are cordially invited to participate in a boxing competition.")
    print("You could win {}x what you wager".format(multiplier))
    time.sleep(1)

    choice = ""
    while choice.lower() not in ["compete", "pass"]:
        print('"Compete" or "pass"?')
        choice = input(">> ")
    
    if choice.lower() == "compete":
        bet = -1
        while bet not in range(0, player.gold + 1):
            print("\nHow much of your gold would you like to wager?")
            print("You have {} gold to wager".format(player.gold))
            try:
                bet = int(input(">> "))
            except:
                bet = -1
        player.gold -= bet
        
        roll = dice.roll(1,20) + player.stat_mod(player.con)
        print("\nCon check:", roll)
        time.sleep(1)
        if roll >= dc:
            print("You win!")
            time.sleep(1)
            reward = bet * multiplier
            print("You win {} gold!".format(reward))
            player.gold += reward
            time.sleep(1)
        else:
            print("You take a beating and go down in the third round")
            damage = 0
            for i in range(math.ceil(player.class_level/2)):
                damage += dice.roll(2,4)
            player.take_damage(damage)
            time.sleep(1)
    else:
        print("\nBest not to risk this pretty face")
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
    print()


def random_encounter(num_combatants: int, player: object, fluff_text: bool=True):
    encounters = []

    if player.class_level <= 4:
        encounters = [goblin_encounter, goblin_horde_encounter]
    elif player.class_level <= 9:
        encounters = [goblin_encounter, goblin_horde_encounter, 
                      wolf_encounter, zombie_encounter]
    elif player.class_level <= 15:
        encounters = [goblin_encounter, goblin_horde_encounter,
                      wolf_encounter, undead_encounter, zombie_encounter]
    elif player.class_level < 20:
        encounters = [goblin_horde_encounter, wolf_encounter,
                      undead_encounter, zombie_horde_encounter, vampire_horde_encounter, vampire_encounter]
    else:
        encounters = [boss_encounter]

    # pick encounter
    randomChoice = random.choice(encounters)

    def goblin():
        print("You see a goblinoid army, before they see you")
        time.sleep(1)
        print("You fire an arrow, scaring most of the army into running")
        time.sleep(1)
        print("The remaining goblinoids turn and attack you")
   
    def wolf():
        print("You hear growling behind you")
        time.sleep(1)
        print("You turn to see wolves prowling nearby")
        time.sleep(1)
        print("Some of them lung at you...")

    def undead():
        print("The smell of rot and death assails your senses")
        time.sleep(1)
        print("You hear a sound behind you, you turn and see...")

    def zombie():
        print("You see the bodies of people who have been fed upon")
        time.sleep(1)
        print("The smell of rot and decay grows stronger")
        time.sleep(1)
        print("You hear groaning in the distance, but, it's too late to run")

    def vampire():
        print("You enter an ornate house")
        time.sleep(1)
        print("The staff seems...sluggish and off")
        time.sleep(1)
        print("Too late you realize the Lord of the House isn't quite human...")

    def final_boss():
        print("Finally, after many trials and tribulations, you reach the Dark Lord's Castle")
        time.sleep(1)
        print("Inside, the place is a mess")
        time.sleep(1)
        print("There is no staff")
        time.sleep(1)
        print("There is blood on the floors and walls")
        time.sleep(1)
        print("You make your way to the Throne Room to find the Lord and his missing staff...")

    def error():
        print("Fluff error")
        sys.exit(1)

    fluff = None
    if randomChoice == goblin_encounter or randomChoice == goblin_horde_encounter:
        fluff = goblin
    elif randomChoice == wolf_encounter:
        fluff = wolf
    elif randomChoice == undead_encounter:
        fluff = undead
    elif randomChoice == zombie_encounter or randomChoice == zombie_horde_encounter:
        fluff = zombie
    elif randomChoice == vampire_encounter or randomChoice == vampire_horde_encounter:
        fluff = vampire
    elif randomChoice == boss_encounter:
        fluff = final_boss
    else:
        fluff = error
    
    return [randomChoice(num_combatants), fluff]


def goblin_encounter(num_of_foes: int):
    """A table for random goblin encounter
    
    includes goblins, hobgoblins, and wolves"""
    encounter = []
    g = 0
    h = 0
    w = 0
    h = 0

    for i in range (num_of_foes):
        rand_num = dice.roll(1, 9)

        if rand_num in [1, 2, 3]:
            g += 1
            encounter.append(e.Goblin(name="Goblin {}".format(g)))
        elif rand_num in [4, 5, 6]:
            h += 1
            encounter.append(e.Hobgoblin(name="Hobgoblin {}".format(h)))
        elif rand_num in [7, 8]:
            w += 1
            encounter.append(e.Wolf(name="Wolf {}".format(w)))
        elif rand_num in [9]:
            h += 1
            encounter.append(e.ArmoredHulk(name="Armored Hobgoblin {}".format(h), damage_reduction=3))
    
    return encounter


def goblin_horde_encounter(num_of_foes: int):
    """A table for random goblin encounter

    includes only goblins"""
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
    """A table for random Zombie horde encounter

    includes 2x as many Zombies"""
    return zombie_encounter(num_of_foes * 2)


def vampire_horde_encounter(num_of_foes: int):
    """a table for a random vampire encounter
    
    includes vampires and a vampire lord"""
    encounter = []
    v = 0
    l = 0

    for i in range(math.ceil(num_of_foes/2)):
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


def vampire_encounter(num_of_foes: int):
    """a table for a random vampire encounter
    
    includes vampires, a vampire lord, and thralls"""
    encounter = []
    v = 0
    l = 0
    t = 0

    for i in range(math.ceil(num_of_foes/2)):
        if l < 1:
            rand_num = dice.roll(1, 4)
            if rand_num == 1:
                l += 1
                encounter.append(e.VampireLord(name="Vampire Lord"))
            elif rand_num == 2:
                v += 1
                encounter.append(e.Vampire(name="Vampire {}".format(v)))
            else:
                t += 1
                encounter.append(e.Thrall(name="Thrall {}".format(t)))
        else:
            if rand_num == 1:
                v += 1
                encounter.append(e.Vampire(name="Vampire {}".format(v)))
            else:
                t += 1
                encounter.append(e.Thrall(name="Thrall {}".format(t)))
    return encounter


def boss_encounter(num_of_foes: int):
    encounter = zombie_horde_encounter(num_of_foes)
    encounter.append(e.Boss(name="The Dark Lord"))

    return encounter
