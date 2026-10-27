class Ticket:
    def __init__(self, film, narx, soni):
        self.film = film
        self.narx = narx
        self.soni = soni

    def total_cost(self):
        return self.narx * self.soni

    def show_info(self):
        print("Film:", self.film)
        print("Umumiy xarajat:", self.total_cost())


ticket = Ticket("Avatar", 40000, 3)
print(ticket.total_cost())
ticket.show_info()