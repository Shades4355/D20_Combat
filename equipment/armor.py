class Armor:
    def __init__(self, name="unarmored", value=0, magic=0, price=0):
        self.name = name
        self.value = value
        self.magic = magic
        self.price = price
        

class Leather(Armor):
    def __init__(self, name="leather armor", value=1, magic=0, price=2):
        super().__init__(name, value, magic, price)


class Hide(Armor):
    def __init__(self, name="hide armor", value=2, magic=0, price=4):
        super().__init__(name, value, magic, price)


class Chain(Armor):
    def __init__(self, name="chain armor", value=3, magic=0, price=6):
        super().__init__(name, value, magic, price)


class Scale(Armor):
    def __init__(self, name="scale armor", value=4, magic=0, price=8):
        super().__init__(name, value, magic, price)


class HalfPlate(Armor):
    def __init__(self, name="half plate", value=5, magic=0, price=10):
        super().__init__(name, value, magic, price)


class FullPlate(Armor):
    def __init__(self, name="full-plate", value=6, magic=0, price=12):
        super().__init__(name, value, magic, price)
