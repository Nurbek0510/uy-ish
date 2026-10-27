class Athlete:
    def __init__(self, ism, sport_turi, yosh):
        self.ism = ism
        self.sport_turi = sport_turi
        self.yosh = yosh

    def show_info(self):
        print("Ism:", self.ism)
        print("Sport turi:", self.sport_turi)
        print("Yosh:", self.yosh)


athlete = Athlete("Ali", "Futbol", 20)
athlete.show_info()