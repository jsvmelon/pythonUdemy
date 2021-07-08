import shelve
import random

help(random.randint)

help(shelve)

for obj in dir(shelve.Shelf):
    if obj[0] != "_":
        print(obj)

# print(dir())
# print(dir(shelve))

# print(dir())
# print(dir(__builtins__))
#
# for m in dir(__builtins__):
#     print(m)
