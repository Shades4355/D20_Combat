import imp
import json
from classes import hero as h
from equipment import weapons as w
from equipment import armor as a

def save(player: object):
    hero_file = open("save_file.json", "w")
    player_weapon = json.JSONEncoder().encode({
        "name": player.weapon.name,
        "magic": player.weapon.magic,
        "num_damage_dice": player.weapon.num_damage_dice,
        "damage_dice": player.weapon.damage_die,
        "special": player.weapon.special
    })

    player_armor = json.JSONEncoder().encode({
        "name": player.armor.name,
        "value": player.armor.value,
        "magic": player.armor.magic,
        "price": player.armor.price
    })

    player_obj = json.JSONEncoder().encode({
        "name": player.name,
        "class_name": player.class_name,
        "class_level": player.class_level,
        "base_health": player.base_health,
        "xp": player.xp,
        "weapon": player_weapon,
        "inventory": player.inventory,
        "special": player.special,
        "armor": player_armor,
        "str": player.str,
        "dex": player.dex,
        "con": player.con,
        "int": player.int,
        "wis": player.wis,
        "cha": player.cha,
        "health": player.health,
        "max_health": player.max_health,
        "gold": player.gold
    })
    hero_file.write(str(player_obj))
    hero_file.close()

def load():
    hero_file = open("save_file.json", "r")
    player = json.load(hero_file)
    hero_file.close()

    player_weapon = json.loads(player["weapon"])

    weapon = w.Weapon(name=player_weapon["name"], magic=player_weapon["magic"], num_damage_dice=player_weapon["num_damage_dice"], damage_die=int(player_weapon["damage_dice"]),special=player_weapon["special"])

    player_armor = json.loads(player["armor"])
    
    armor = a.Armor(name=player_armor["name"], value=player_armor["value"], magic=player_armor["magic"], price=player_armor["price"])

    hero = h.Hero(name=player['name'],
        class_name=player["class_name"],
        class_level=int(player["class_level"]),
        base_health=int(player["base_health"]),
        xp=int(player["xp"]),
        weapon=weapon,
        inventory=player["inventory"],
        special=player["special"],
        armor=armor,
        str=int(player["str"]),
        dex=int(player["dex"]),
        con=int(player["con"]),
        int=int(player["int"]),
        wis=int(player["wis"]),
        cha=int(player["cha"]),
        health=player["health"],
        max_health=player["max_health"],
        gold=int(player["gold"])
    )

    return hero
