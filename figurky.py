class Figurka:
    def __init__(self, color, priority=1, hp=100):
        self.color = color
        self.priority = priority
        self.hp = hp

    def die(self):
        self.hp = 0