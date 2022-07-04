
class Weapon():
    def __init__(self, name="weapon", magic=0, num_damage_dice=1, damage_die=4, special=[], damage_type="bludgeoning"):
        self.name = name
        self.magic = magic
        self.num_damage_dice = num_damage_dice
        self.damage_die = damage_die
        self.special = special
        self.damage_type = damage_type


class Unarmed(Weapon):
    def __init__(self, name="unarmed strikes", magic=2, num_damage_dice=1, damage_die=4, special=["flurry"], damage_type="bludgeoning"):
        super().__init__(name, magic, num_damage_dice, damage_die, special, damage_type)


class ShortSword(Weapon):
    def __init__(self, name="short sword", magic=1, num_damage_dice=1, damage_die=6, special=["back stab"], damage_type="piercing"):
        super().__init__(name, magic, num_damage_dice, damage_die, special, damage_type)


class LongSword(Weapon):
    def __init__(self, name="long sword", magic=0, num_damage_dice=2, damage_die=4, special=[], damage_type="slashing"):
        super().__init__(name, magic, num_damage_dice, damage_die, special, damage_type)


class HandAxe(Weapon):
    def __init__(self, name="hand axe", magic=0, num_damage_dice=1, damage_die=8, special=["cleave"], damage_type="slashing"):
        super().__init__(name, magic, num_damage_dice, damage_die, special, damage_type)


class Poleaxe(Weapon):
    def __init__(self, name="poleaxe", magic=0, num_damage_dice=1, damage_die=10, special=["cleave"], damage_type="slashing"):
        super().__init__(name, magic, num_damage_dice, damage_die, special, damage_type)


class Staff(Weapon):
    def __init__(self, name="staff", magic=0, num_damage_dice=1, damage_die=4, special=["fireball"], damage_type="magic"):
        super().__init__(name, magic, num_damage_dice, damage_die, special, damage_type)


class Rod(Weapon):
    def __init__(self, name="rod", magic=0, num_damage_dice=1, damage_die=6, special=["magic missile"], damage_type="bludgeoning"):
        super().__init__(name, magic, num_damage_dice, damage_die, special, damage_type)
