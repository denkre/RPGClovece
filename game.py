from figurky import Figurka
from queue import Queue

from random import randint, choice


class HerniPole:
    SIZE = 40
    COLORS = ["RED", "GREEN", "YELLOW", "BLUE"]

    def __init__(self):
        self.kostka = Kostka()
        self.hraci = []
        self.pole = []
        self.start_policka = {}
        self.fin_policka = {}

        self.gen_pole()
        self.add_hrace()

    def add_hrace(self):
        for color in HerniPole.COLORS:
            self.hraci.append(Hrac(color))

    def print_hrace(self):
        print("HRACI")
        for hrac in self.hraci:
            print(hrac.color)
            print("Figurky:")
            for figurka in hrac.act_figurky:
                print(f" - {figurka}")
        print()

    def gen_pole(self):
        for hrac in self.hraci:
            start_policko = Policko(is_special=True, color=hrac.color)
            hrac.start_domecek.set_start_policko(start_policko)
            hrac.set_start_index(len(self.pole))
            self.pole.append(start_policko)
            self.start_policka[hrac] = start_policko

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

            fin_policko = Policko(is_special=True, color=hrac.color)
            hrac.fin_domecek.set_fin_policko(fin_policko)
            hrac.set_fin_index(len(self.pole))
            self.fin_policka[hrac.color] = fin_policko
            self.pole.append(fin_policko)

    def print_pole(self):
        print("HERNI POLE")
        for policko in self.pole:
            print(policko)
        print()

    def game(self):
        while True:
            self.play_round()

    def play_round(self):
        for hrac in self.hraci:
            hrac.sort_figurky()

            # tah figurkou
            act_figurka = hrac.act_figurky.dequeue()
            num = self.kostka.hod()
            if act_figurka.index:
                next_index = act_figurka.index + num
                fin_distance = act_figurka.get_fin_distance(next_index)
                if  fin_distance > 0:
                    # bez dopredu a nastav policku figurku
                    ...
                elif fin_distance == 0:
                    # bez dopredu a nastav policku figurku
                    ...
                else:
                    # prepocitej a pripadne bez do domecku
                    ...
            hrac.figurky.enqueue(act_figurka)


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
    def __init__(self, hrac):
        self.hrac = hrac
        self.color = hrac.color
        self.pole = [Policko() for _ in range(4)]
        self.fin_policko = None

    def set_fin_policko(self, policko):
        self.fin_policko = policko

    def place_figurka(self, figurka, index):
        policko = self.pole[index]
        if not policko.figurky:
            policko.figurky.append(figurka)
        else:
            raise Exception("Pole je již obsazeno!")

    def can_place_figurka(self, index):
        policko = self.pole[index]
        if policko.figurky:
            return False
        else:
            return True

    def __str__(self):
        return f"Finish domecek of {self.color}"


class StartDomecek:
    def __init__(self, hrac):
        self.hrac = hrac
        self.color = hrac.color
        self.pole = []
        self.start_policko = None

    def set_start_policko(self, policko):
        self.start_policko = policko

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
    def __init__(self, color):
        self.color = color
        self.figurky = [Figurka(self.color) for _ in range(4)]
        self.act_figurky = Queue(4, items=self.figurky)
        self.start_domecek = StartDomecek(self)
        self.fin_domecek = FinDomecek(self)

    def add_figurky_to_start_domecek(self):
        ...

    def sort_figurky(self):
        # radici algoritmus figurek
        self.act_figurky.sort()

    def set_start_index(self, index):
        self.start_index = index

    def set_fin_index(self, index):
        self.fin_index = index


def run():
    board = HerniPole()
    board.print_hrace()
    # board.print_pole()
