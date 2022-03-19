from figurky import Figurka

from random import randint, choice


class HerniPole:
    SIZE = 40
    COLORS = ["RED", "GREEN", "YELLOW", "BLUE"]

    def __init__(self):
        self.kostka = Kostka()
        self.hraci = ...
        self.pole = []
        self.start_policka = {}
        self.fin_policka = {}

    def gen_pole(self):
        for color in self.COLORS:
            start_policko = Policko(is_special=True, color=color)
            self.pole.append(start_policko)
            self.start_policka[color] = start_policko

            for i in range(self.SIZE//4-2):
                rand = randint(1, 100)
                if rand % 10 == 0:
                    policko = HealPolicko()
                elif rand % 10 == 1:
                    policko = ManaPolicko()
                elif rand % 20 == 2:
                    policko = KillPolicko()
                else:
                    policko = Policko()
                self.pole.append(policko)

            fin_policko = Policko(is_special=True, color=color)
            self.fin_policka[color] = fin_policko
            self.pole.append(fin_policko)


class Policko:
    def __init__(self, is_special=False, color=None):
        self.is_special = is_special
        self.has_effect = False
        if color:
            self.color = color
        self.figurky = []

    def __str__(self):
        return "Policko"


# class FinPolicko(Policko):
#     def __init__(self, color):
#         super().__init__()
#         self.is_special = True
#         self.has_effect = False
#         self.color = color
#
#     def __str__(self):
#         return f"FinPolicko of {self.color}"


class ManaPolicko(Policko):
    MANA_AMOUNT = 20

    def __init__(self):
        super().__init__()
        self.is_special = True
        self.has_effect = True

    def effect(self, figurka):
        figurka.mana += self.MANA_AMOUNT

    def __str__(self):
        return "+ Mana Policko"


class HealPolicko(Policko):
    HP_AMOUNT = 20

    def __init__(self):
        super().__init__()
        self.is_special = True
        self.has_effect = True

    def effect(self, figurka):
        figurka.hp += self.HP_AMOUNT

    def __str__(self):
        return "Heal Policko"


class KillPolicko(Policko):
    def __init__(self):
        super().__init__()
        self.is_special = True
        self.has_effect = True

    def effect(self, figurka):
        figurka.die()

    def __str__(self):
        return "Kill Policko"


class FinDomecek:
    def __init__(self, color):
        self.color = color
        self.pole = [Policko() for i in range(4)]

    def place_figurka(self, figurka, index):
        policko = self.pole[index]
        if not policko.figurky:
            policko.figurky.append(figurka)
        else:
            raise Exception("Pole je již obsazeno!")

    def can_place_figurka(self, figurka, index):
        policko = self.pole[index]
        if policko.figurky:
            return False
        else:
            return True

    def __str__(self):
        return f"Finish domecek of {self.color}"


class StartDomecek:
    def __init__(self, color):
        self.color = color
        self.pole = []

    def add_figurka(self, figurka):
        self.pole.append(figurka)

    def __str__(self):
        return f"Start domecek of {self.color}"
    

class Kostka:
    def __init__(self, sides=6):
        self.sides = sides

    def hod(self):
        return randint(1, self.sides)


class Hrac:
    def __init__(self):
        self.figurky = ...

    def sort_figurky(self):
        # řadící algoritmus figurek
        ...



