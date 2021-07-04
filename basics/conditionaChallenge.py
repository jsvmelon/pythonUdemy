name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 18 or age > 30:
    print("Hello {}, you are not in the right age bracket".format(name))
else:
    print("Welcome {}".format(name))
