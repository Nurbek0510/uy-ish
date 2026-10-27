class Player:
    def __init__(self, ism):
        self.ism = ism
        self.energiya = 100

    def use_energy(self, amount):
        self.energiya -= amount

        if self.energiya < 0:
            self.energiya = 0

    def show_status(self):
        print("O'yinchi:", self.ism)
        print("Energiya:", self.energiya)


player = Player("Hero")
player.use_energy(35)
player.show_status()