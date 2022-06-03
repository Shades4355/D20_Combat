import random

class Misc:
    def roll(self, num, die):
        total = 0
        for dice in range(0, num):
            total += random.randrange(1, die + 1)
        return round(total)

