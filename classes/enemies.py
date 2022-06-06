import classes.utility_functions as utils


class Enemy():
    def __init__(self, name='template', health=1, attack=0, armor=0, damage_die=4, lives=1, grantXP=1, loot=1, damage_reduction=0):
        self.name = name
        self.max_hit_points = health
        self.current_hit_points = health
        self.attack = attack
        self.ac = 10 + armor
        self.damage_reduction = damage_reduction
        self.damage_die = damage_die
        self.grantXP = grantXP
        self.loot = loot
        self.lives = lives
        self.alive = True
    
    def do_damage(self):
        dice = utils.Util()
        return dice.roll(1, self.damage_die)

    def take_damage(self, damage):
        post_DR_damage = damage - self.damage_reduction
        if post_DR_damage > 0:
            hurt = self.current_hit_points - post_DR_damage
        else:
            hurt = 0
            
        remaining_points = self.current_hit_points - hurt
        if remaining_points > 0:
            self.current_hit_points = remaining_points
            print("{} took {} damage, and have {} left".format(
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
        

    

