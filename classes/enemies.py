import math, sys
from classes import dice


class Enemy():
    def __init__(self, name="template", hit_die=4, attack_bonus=2, armor=0, number_of_damage_die=1, damage_die=4, level=1, lives=1, grantXP=1, damage_reduction=0, str_mod=0, dex_mod=0, con_mod=0, loot=1):
        self.name = name
        self.level = level
        self.hit_die = hit_die
        self.str_mod = str_mod
        self.dex_mod = dex_mod
        self.con_mod = con_mod
        self.max_hit_points = self.get_max_health()
        self.current_hit_points = self.max_hit_points
        self.attack_bonus = attack_bonus
        self.ac = 10 + armor + dex_mod
        self.damage_reduction = damage_reduction
        self.number_of_damage_die = number_of_damage_die
        self.damage_die = damage_die
        self.grantXP = grantXP
        self.lives = lives
        self.alive = True
        self.loot = loot


    def attack(self, player: object):
        roll = dice.roll(1, 20)
        attack_roll = roll + self.attack_bonus + self.str_mod

        damage = 0
        if roll == 20:
            damage = self.do_damage(True)
            print("Critical!")
            player.take_damage(damage)
        elif attack_roll > player.ac:
            damage = self.do_damage(False)
            player.take_damage(damage)
        else:
            print(self.name, "missed", player.name)

    def do_damage(self, crit:bool):
        if crit == True:
            return dice.roll(self.number_of_damage_die, self.damage_die) + dice.roll(self.number_of_damage_die, self.damage_die) + self.str_mod
        else:
            return dice.roll(self.number_of_damage_die, self.damage_die) + self.str_mod

    def get_max_health(self):
        hit_points = 0
        for i in range(self.level):
            hit_points += dice.roll(1, self.hit_die) + self.con_mod
        return hit_points

    def take_damage(self, damage:int):
        post_DR_damage = damage - self.damage_reduction
        if post_DR_damage > 0:
            if self.current_hit_points - post_DR_damage > 0:
                hurt = post_DR_damage
            else:
                hurt = self.current_hit_points
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
    

class Goblin(Enemy):
    def __init__(self, name="Goblin", health=3, attack_bonus=0, armor=0, number_of_damage_die=1, damage_die=4, level=1, lives=1, grantXP=1, damage_reduction=0, str_mod=-1, dex_mod=2, con_mod=0):
        super().__init__(name, health, attack_bonus, armor, number_of_damage_die, damage_die,
                         level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class Hobgoblin(Goblin):
    def __init__(self, name="Hobgoblin", health=6, attack_bonus=2, armor=0, number_of_damage_die=1, damage_die=4, level=2, lives=1, grantXP=1, damage_reduction=0, str_mod=1, dex_mod=1, con_mod=1):
        super().__init__(name, health, attack_bonus, armor, number_of_damage_die, damage_die,
                         level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class Wolf(Enemy):
    def __init__(self, name="Wolf", health=6, attack_bonus=3, armor=0, number_of_damage_die=1, damage_die=6, level=2, lives=1, grantXP=2, damage_reduction=0, str_mod=1, dex_mod=2, con_mod=1):
        super().__init__(name, health, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class DireWolf(Wolf):
    def __init__(self, name="Dire Wolf", health=8, attack_bonus=2, armor=0, number_of_damage_die=2, damage_die=4, level=3, lives=1, grantXP=2, damage_reduction=0, str_mod=3, dex_mod=2, con_mod=2):
        super().__init__(name, health, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class Undead(Enemy):
    def __init__(self, name="Undead Template", hit_die=6, attack_bonus=2, armor=3, number_of_damage_die=1, damage_die=4, level=3, lives=1, grantXP=2, damage_reduction=0, str_mod=0, dex_mod=0, con_mod=0):
        super().__init__(name, hit_die, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class Zombie(Undead):
    def __init__(self, name="Zombie", hit_die=6, attack_bonus=2, armor=3, number_of_damage_die=1, damage_die=6, level=3, lives=1, grantXP=2, damage_reduction=0, str_mod=1, dex_mod=-2, con_mod=3):
        super().__init__(name, hit_die, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)

    def take_damage(self, damage: int):
        post_DR_damage = damage - self.damage_reduction
        if post_DR_damage > 0:
            if self.current_hit_points - post_DR_damage > 0:
                hurt = post_DR_damage
            else:
                hurt = self.current_hit_points
        else:
            hurt = 0

        remaining_points = self.current_hit_points - hurt
        if remaining_points > 0:
            self.current_hit_points = remaining_points
            print("{} took {} damage, and have {} HP left".format(
                self.name, hurt, self.current_hit_points))
        else:
            revival_chance = dice.roll(1, 20) + self.con_mod
            if revival_chance >= damage + 5:
                self.current_hit_points = 1
                print("{0.name} got back up, albeit damaged".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.current_hit_points = 0
                self.alive = False


class Skeleton(Undead):
    def __init__(self, name="Skeleton", hit_die=8, attack_bonus=4, armor=3, number_of_damage_die=1, damage_die=6, level=2, lives=2, grantXP=3, damage_reduction=2, str_mod=0, dex_mod=2, con_mod=2):
        super().__init__(name, hit_die, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class Ghoul(Undead):
    def __init__(self, name="Ghoul", hit_die=8, attack_bonus=1, armor=3, number_of_damage_die=2, damage_die=4, level=5, lives=1, grantXP=2, damage_reduction=1, str_mod=1, dex_mod=2, con_mod=0):
        super().__init__(name, hit_die, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class Vampire(Undead):
    def __init__(self, name="Vampire", hit_die=6, attack_bonus=3, armor=3, number_of_damage_die=1, damage_die=6, level=3, lives=2, grantXP=2, damage_reduction=2, str_mod=4, dex_mod=4, con_mod=4):
        super().__init__(name, hit_die, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)

    def attack(self, player: object):
        roll = dice.roll(1, 20)
        attack_roll = roll + self.attack_bonus + self.str_mod

        damage = 0
        if roll == 20:
            damage = self.do_damage(True)
            print("Critical!")
            player.take_damage(damage)
        elif attack_roll > player.ac:
            damage = self.do_damage(False)
            player.take_damage(damage)
        else:
            print(self.name, "missed", player.name)

        if damage > 0:
           self.heal_self(math.floor(damage/2))

    def heal_self(self, amount:int):
        health = self.current_hit_points + amount
        
        if health > self.max_hit_points:
            health = self.max_hit_points
        
        self.current_hit_points = health

        print("{0} healed {1} HP from drinking your blood".format(self.name, amount))


class VampireLord(Vampire):
    def __init__(self, name="Vampire Lord", hit_die=6, attack_bonus=4, armor=3, number_of_damage_die=1, damage_die=8, level=5, lives=3, grantXP=4, damage_reduction=2, str_mod=4, dex_mod=4, con_mod=4):
        super().__init__(name, hit_die, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)

    def attack(self, player: object):
        roll = dice.roll(1, 20)
        attack_roll = roll + self.attack_bonus + self.str_mod

        damage = 0
        if roll == 20:
            damage = self.do_damage(True)
            print("Critical!")
            player.take_damage(damage)
        elif attack_roll > player.ac:
            damage = self.do_damage(False)
            player.take_damage(damage)
        else:
            print(self.name, "missed", player.name)

        if damage > 0:
            self.heal_self(damage)


class Thrall(Vampire):
    def __init__(self, name="Thrall", hit_die=4, attack_bonus=3, armor=3, number_of_damage_die=1, damage_die=4, level=2, lives=1, grantXP=2, damage_reduction=2, str_mod=3, dex_mod=3, con_mod=3):
        super().__init__(name, hit_die, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)


class Boss(VampireLord):
    def __init__(self, name="Final Boss", hit_die=8, attack_bonus=5, armor=3, number_of_damage_die=2, damage_die=6, level=10, lives=2, grantXP=0, damage_reduction=3, str_mod=5, dex_mod=5, con_mod=5):
        super().__init__(name, hit_die, attack_bonus, armor, number_of_damage_die, damage_die, level, lives, grantXP, damage_reduction, str_mod, dex_mod, con_mod)

    def take_damage(self, damage: int):
        post_DR_damage = damage - self.damage_reduction
        if post_DR_damage > 0:
            if self.current_hit_points - post_DR_damage > 0:
                hurt = post_DR_damage
            else:
                hurt = self.current_hit_points
        else:
            hurt = 0

        remaining_points = self.current_hit_points - hurt
        if remaining_points > 0:
            self.current_hit_points = remaining_points
            print("{} took {} damage, and have {} HP left".format(
                self.name, hurt, self.current_hit_points))
        else:
            revival_chance = dice.roll(1, 20) + self.con_mod
            if revival_chance >= damage + 3:
                self.current_hit_points = dice.roll(1,6)
                print("{0.name} got back up, albeit damaged".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.current_hit_points = 0
                self.alive = False
                print("You Win!")
                input("[Enter]")
                sys.exit(0)
