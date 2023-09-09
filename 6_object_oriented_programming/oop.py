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

print(f"Models: {CS.make} = {CS.price}, {DevOps.make} = {DevOps.price}")

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format{CS, DevOps})

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class
Instantiate: create an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
"""