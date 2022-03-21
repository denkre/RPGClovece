class Figurka:
    def __init__(self, color, priority=1, hp=100):
        self.color = color
        self.priority = priority
        self.hp = hp

    def die(self):
        self.hp = 0

    def set_index(self, index):
        self.index = index

    def get_fin_distance(self, index=self.index):
        ...