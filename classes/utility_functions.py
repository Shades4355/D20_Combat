import random


class Util:
    def roll(self, num, die):
        total = 0
        for i in range(0, num):
            total += random.randrange(1, die + 1)
        return round(total)
