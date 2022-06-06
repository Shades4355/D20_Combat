import classes.utility_functions as utils


class Enemy():
    def __init__(self, name='template', hit_die=4, attack_bonus=0, armor=0, number_of_damage_die=1, damage_die=4, level=1, lives=1, grantXP=1, damage_reduction=0, str_mod=0, dex_mod=0, con_mod=0):
        self.name = name
        self.level = level
        self.hit_die = hit_die
        self.max_hit_points = self.get_max_health()
        self.current_hit_points = self.max_hit_points
        self.attack_bonus = attack_bonus
        self.ac = 10 + armor
        self.damage_reduction = damage_reduction
        self.number_of_damage_die = number_of_damage_die
        self.damage_die = damage_die
        self.grantXP = grantXP
        self.loot = loot
        self.lives = lives
        self.alive = True
        self.str_mod = str_mod
        self.dex_mod = dex_mod
        self.con_mod = con_mod

    def do_damage(self, crit:bool, stat_mod:int):
        dice = utils.Util()
        if crit == True:
            return dice.roll(self.number_of_damage_die, self.damage_die) + dice.roll(self.number_of_damage_die, self.damage_die) + stat_mod
        else:
            return dice.roll(self.number_of_damage_die, self.damage_die) + stat_mod

    def take_damage(self, damage:int):
        post_DR_damage = damage - self.damage_reduction
        if post_DR_damage > 0:
            hurt = self.current_hit_points - post_DR_damage
        else:
            hurt = 0

        remaining_points = self.current_hit_points - hurt
        if remaining_points > 0:
            self.current_hit_points = remaining_points
            print("{} took {} damage, and have {} HP left".format(
                self.name, hurt, self.current_hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                self.current_hit_points = self.max_hit_points
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.current_hit_points = 0
                self.alive = False
    
    def get_max_health(self):
        util_functions = utils.Util()
        hit_points = 0
        for i in range(self.level):
            hit_points += util_functions(1, self.hit_die) + self.con_mod
        return hit_points

    def attack(self, player_ac:int, stat_mod:int):
        dice = utils.Util()
        roll = dice.roll(1, 20)

        attack_roll = roll + self.attack_bonus
        damage = 0
        if roll == 20:
            self.do_damage(True, stat_mod)
        elif attack_roll > player_ac:
            self.do_damage(False, stat_mod)

        return damage


class Goblin(Enemy):
    def __init__(self, name='Goblin', health=1, attack_bonus=0, armor=0, number_of_damage_die=1, damage_die=4, level=1, lives=1, grantXP=1, damage_reduction=0):
        super().__init__(name, health, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction)


class Hobgoblin(Goblin):
    def __init__(self, name='Hobgoblin', health=1, attack_bonus=1, armor=0, number_of_damage_die=1, damage_die=4, level=2, lives=1, grantXP=1, damage_reduction=0):
        super().__init__(name, health, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction)


class Wolf(Enemy):
    def __init__(self, name='Wolf', health=4, attack_bonus=1, armor=0, number_of_damage_die=2, damage_die=4, level=2, lives=1, grantXP=2, damage_reduction=0, str_mod=0, dex_mod=0, con_mod=2):
        super().__init__(name, health, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class DireWolf(Wolf):
    def __init__(self, name='Dire Wolf', health=4, attack_bonus=5, armor=0, number_of_damage_die=2, damage_die=4, level=2, lives=1, grantXP=2, damage_reduction=0, str_mod=3, dex_mod=2, con_mod=2):
        super().__init__(name, health, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


