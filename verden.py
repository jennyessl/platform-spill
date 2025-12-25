import keyboard, time, os
    
class Verden:
    def clear_terminal(self):
        _ = os.system('cls')

    def __init__(self, level):
        self._level = level
        self._rutenett = []
        for linje in level:
            liste = []
            for celle in linje:
                liste.append(celle)
            self._rutenett.append(liste)
        self._rutenett[13][1] = "O"

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

    def beveg_tick(self):
            start = time.time()
            while time.time() - start < 0.15:
                key = keyboard.read_key()
                if key == "a":
                    self.beveg(-1, 0) 
                    break
                if key == "d":
                    self.beveg(1, 0)
                    break
                if key == "esc":
                    status = False
                if key == "w":
                    key2 = keyboard.read_key()
                    start = time.time()
                    for n in range (2):
                            self.beveg(0, -1)
                            self.skriv_ut()
                    if key2 == "d":
                        self.beveg(2, 0)
                        break
                    if key2 == "a":
                        self.beveg(-2, 0)
                        break
                    else:
                        break

    def fall(self):
        for n in range(14):
            forrige = self.rad()
            self.skriv_ut()
            self.beveg(0, 1)
            if forrige == self.rad():
                break
            time.sleep(0.1)
        self.skriv_ut()

    def start_spill(self):
        status = True
        self.skriv_ut()
        while status == True:
            self.beveg_tick()
            self.fall()
            if self.sjekk_doed():
                return False
            if self.sjekk_vinn():
                return True