import keyboard, time, os
from test_level import liste
    
class Verden:
    def clear_terminal(self):
        _ = os.system('cls')

    def __init__(self, level_animasjon, x, y):
        self._teller = 0
        self._level_animasjon = level_animasjon
        self._level = level_animasjon[0]
        self._rutenett = []
        for linje in self._level:
            liste = []
            for celle in linje:
                liste.append(celle)
            self._rutenett.append(liste)
        self._rutenett[y][x] = "O"
        self._hopper = False

    def skriv_ut(self):
        self.clear_terminal()
        for linje in self._rutenett:
            for celle in linje:
                print(celle, end = "")
            print()

    def rad(self):
        teller = 0
        for rad in self._rutenett:
            if "O" in rad:
                return teller
            teller += 1
        return None

    def kolonne(self):
        teller = 0
        for rad in self._rutenett:
            teller = 0
            for celle in rad:
                if celle == "O":
                    return teller
                teller += 1
        return None

    def beveg(self, rettning_x, rettning_y):
        forrigex = self.kolonne()
        forrigey = self.rad()
        if self._rutenett[forrigey + rettning_y][forrigex + rettning_x] == " ":
            self._rutenett[forrigey + rettning_y][forrigex + rettning_x] = "O"
            self._rutenett[forrigey][forrigex] = " "
        
    def sjekk_doed(self):
        if self._rutenett[self.rad() + 1][self.kolonne()] == "Ʌ":
            return True
        return False
    
    def sjekk_vinn(self):
        if self._rutenett[self.rad() + 1][self.kolonne()] == "I":
            return True
        return False

    def beveg_rutenett(self, status):
        if status == "o":
            self._teller += 1
            self._level = self._level_animasjon[self._teller]
            x = self.kolonne()
            y = self.rad()
            self._rutenett.clear()
            for linje in self._level:
                liste = []
                for celle in linje:
                    liste.append(celle)
                self._rutenett.append(liste)
            if self._teller == len(self._level_animasjon) -1:
                status = "n"
        else:
            self._teller = self._teller - 1
            self._level = self._level_animasjon[self._teller]
            x = self.kolonne()
            y = self.rad()
            self._rutenett.clear()
            for linje in self._level:
                liste = []
                for celle in linje:
                    liste.append(celle)
                self._rutenett.append(liste)
            if self._teller == 0:
                status = "o"
        if self._rutenett[y][x] == "¯":
            self._rutenett[y - 1][x] = "O"
        else:
            self._rutenett[y][x] = "O"
        self.beveg(0, 1)
        return status
    
    def beveg_tick(self):
        self._hopper = False
        start = time.time()
        while time.time() - start < 0.2:
            if keyboard.is_pressed("a"):
                self.beveg(-1, 0)
                time.sleep(0.2 - time.time() + start)
                return True
            if keyboard.is_pressed("d"):
                self.beveg(1, 0)
                time.sleep(0.2 - time.time() + start)
                return True
            if keyboard.is_pressed("esc"):
                return False
            if keyboard.is_pressed("w") and not self._hopper:
                self._hopper = True
                start = time.time()
                for n in range (2):
                        self.beveg(0, -1)
                        self.skriv_ut()
                if keyboard.is_pressed("d"):
                    self.beveg(2, 0)
                    time.sleep(0.2 - time.time() + start)
                    return True
                if keyboard.is_pressed("a"):
                    self.beveg(-2, 0)
                    time.sleep(0.2 - time.time() + start)
                    return True
        return True
                    
    def start_spill(self):
        s = "o"
        status = True
        self.skriv_ut()
        while status == True:
            status = self.beveg_tick()
            self.skriv_ut()
            self.beveg(0,1)
            if self.sjekk_doed():
                return False
            if self.sjekk_vinn():
                return True
            s = self.beveg_rutenett(s)
            self.skriv_ut()
            
Verden(liste, 1, 3).start_spill()