# Object Oriented Programming in Python



class Programmer(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

CS = Programmer("CS", 5000)
print(CS.make)
print(CS.price)

CS.price = 6000
print(CS.price)

DevOps = Programmer("DevOps", 7000)