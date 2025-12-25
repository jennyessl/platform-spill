from verden import Verden
from level_liste import level_liste
class Lobby:
    def __init__(self, level_liste):
        self._level_liste = level_liste
        self._level = 0

    def neste_level(self):
        self._level += 1

    def start_level(self):
        print("level: ", self._level + 1)
        if Verden(self._level_liste[self._level]).start_spill():
            print("level complete")
            self._level += 1
            inp = input("press 1 for next level, 2 for quit: ")
            while inp != "1" and inp != "2":
                inp = input("not valid input: press 1 for next level, 2 for quit: ")
            if inp == "1":
                self.start_level()
        else:
            print("level fail")
            inp = input("press 1 for retry, 2 for quit: ")
            while inp != "1" and inp != "2":
                inp = input("not valid input: press 1 for retry, 2 for quit: ")
            if inp == "1":
                self.start_level()
    
Lobby(level_liste).start_level()