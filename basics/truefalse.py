day = "Friday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")
    
#

if 0:
    print("True")
else:
    print("False")

name = input("Name:")
#if name:
if name != "":
    print("Hello {0}".format(name))
else:
    print("Are you a person with no name?")