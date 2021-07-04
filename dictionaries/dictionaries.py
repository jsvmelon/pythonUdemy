fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# different view types and conversions
print(fruit)
print(fruit.items())  # ItemsView
f_tuple = tuple(fruit.items())  # make it a tuple
print(f_tuple)

print(dict(f_tuple))  # convert to a dictionary

print("-" * 20)

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

print("-" * 20)

for val in fruit.values():
    print(val)

print("-" * 20)

# more efficient
for key in fruit:
    print(fruit[key])

print("-" * 20)

ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f)

print("-" * 20)

for snack in fruit:
    print(snack)

print("-" * 20)

print(fruit["lime"])
while True:
    dict_key = input("enter fruit: ")
    if dict_key == "quit":
        break
    elif dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a {}".format(dict_key))
