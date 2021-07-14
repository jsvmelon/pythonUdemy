# a = 12
# b = 4
# print(a+b)
# print(a.__add__(b))


class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        if self.on:
            print("The kettle is already on")
        else:
            self.on = True

    def switch_off(self):
        if not self.on:
            print("The kettle is already off")
        else:
            self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make, kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.make, hamilton.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# a little bit more readable
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

# using the instance
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# alternatively we can use the class method with an instance as parameter
print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

# objects are dynamic - we can even add an attribute without defining it in the class definition
kenwood.power = 1.5
print(kenwood.power)

# hamilton does not have the attribute ...
# print(hamilton.power)
