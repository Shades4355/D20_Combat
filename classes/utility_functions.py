import random


class Util:
    def roll(self, num, die):
        """function for rolling dice
        
        num: number of dice to roll
        die: type of die to roll (20 = d20; 6 = d6; etc)"""
        total = 0
        for i in range(0, num):
            total += random.randrange(1, die + 1)
        return round(total)
