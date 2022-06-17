
class Weapon():
    def __init__(self, name="weapon", magic=0, num_damage_dice=1, damage_die=4, special=[]):
        self.name = name
        self.magic = magic
        self.num_damage_dice = num_damage_dice
        self.damage_die = damage_die
        self.special = special


class Unarmed(Weapon):
    def __init__(self, name="unarmed strikes", magic=2, num_damage_dice=1, damage_die=4, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class ShortSword(Weapon):
    def __init__(self, name="short sword", magic=1, num_damage_dice=1, damage_die=6, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class LongSword(Weapon):
    def __init__(self, name="long sword", magic=0, num_damage_dice=2, damage_die=4, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class HandAxe(Weapon):
    def __init__(self, name="hand axe", magic=0, num_damage_dice=1, damage_die=8, special=[]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class Poleaxe(Weapon):
    def __init__(self, name="poleaxe", magic=0, num_damage_dice=1, damage_die=10, special=["cleave"]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


class Staff(Weapon):
    def __init__(self, name="Weapon", magic=0, num_damage_dice=1, damage_die=4, special=["fireball"]):
        super().__init__(name, magic, num_damage_dice, damage_die, special)


