import classes.utility_functions as utils
dice = utils.Util()


class Potion:
    """template for healing potions"""

    def __init__(self, name, level, die):
        self.name = name
        self.level = level
        self.die = die
    
    def heal(self, player: object):
        heal = dice.roll(self.level, self.die) + self.level
        if player.health + heal >= player.max_health:
            heal = player.max_health - player.health
        print("{} healed for {} hit points".format(player.name, heal))
        player.health += heal


class Cure_Light(Potion):
    """The weakest of healing potions"""

    def __init__(self, name="cure light potion", level=2, die=4):
        super().__init__(name, level, die)


class Cure_Moderate(Potion):
    """A medium strength healing potion"""

    def __init__(self, name="cure moderate potion", level=4, die=4):
        super().__init__(name, level, die)


class Cure_Serious(Potion):
    """The strongest of healing potions"""

    def __init__(self, name="cure serious potion", level=8, die=4):
        super().__init__(name, level, die)