class Scroll:
    def __init__(self, name="Scroll Template"):
        self.name = name

class Escape(Scroll):
    def __init__(self, name="Scroll of Escape"):
        super().__init__(name)
    
    def escape(self, player):
        player.in_fight = False