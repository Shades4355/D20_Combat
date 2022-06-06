
from array import array


class Weapon():
    def __init__(self, name="Weapon", magic=0, num_damage_dice=1, damage_die=4, special=[]):
        self.name = name
        self.magic = magic
        self.num_damage_dice = num_damage_dice
        self.damage_die = damage_die
        self.special = special


class Unarmed(Weapon):
    def __init__(self, name="Unarmed Strikes", magic=0, num_damage_dice=1, damage_die=4, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class ShortSword(Weapon):
    def __init__(self, name="Short Sword", magic=0, num_damage_dice=1, damage_die=6, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class LongSword(Weapon):
    def __init__(self, name="Long Sword", magic=0, num_damage_dice=2, damage_die=4, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class HandAxe(Weapon):
    def __init__(self, name="Hand Axe", magic=0, num_damage_dice=1, damage_die=8, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class Poleaxe(Weapon):
    def __init__(self, name="Poleaxe", magic=0, num_damage_dice=1, damage_die=10, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class Staff(Weapon):
    def __init__(self, name="Weapon", magic=0, num_damage_dice=1, damage_die=4, special=["Fireball"]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


