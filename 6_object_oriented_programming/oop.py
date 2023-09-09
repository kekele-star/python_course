# Object Oriented Programming in Python
class Programmer(object):

    power_source = "coding"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


cs = Programmer("cs", 5000)
print(cs.make)
print(cs.price)

cs.price = 6000
print(cs.price)

devOps = Programmer("devOps", 7000)

print(f"Models: {cs.make} = {cs.price}, {devOps.make} = {devOps.price}")

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format({cs, devOps}))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class
Instantiate: create an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
"""

print(cs.on)
cs.switch_on()
print(cs.on)

Programmer.switch_on(cs)
print(cs.on)
cs.switch_on()

print("*" * 80)

cs.power = 1.5
print(cs.power)
#print(devOps.power)

print(Programmer.power_source)
print(cs.power_sauce)
print(devOps.power_source)

