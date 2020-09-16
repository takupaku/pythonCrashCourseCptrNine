from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self):
        self.flavours=['vanilla','mango','dark chocolate']
        #super().__init__(restaurant_name='',cuisine_type='')

    def display_flavour(self):
        for flavour in self.flavours:
            print(flavour)

icecreamStand=IceCreamStand()
icecreamStand.display_flavour()
