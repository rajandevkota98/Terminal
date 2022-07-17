class car:
    def __init__(self, body, model, price):
        self.model = model
        self.body = body
        self.price = price

    def milage(self):
        print('milage of this car')



class tata(car):
    pass

p = car('new', 'A1', 1234)

t = tata('1', 'A1', 1234)




t.milage()