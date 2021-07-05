import shelve

# shelves behave like a dictionary
with shelve.open("ShelfTest") as fruit:
    fruit["orange"] = "a sweet, orange citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow citrus fruit"
    fruit["grape"] = "a small, sweet fruit growing in bunches"
    fruit["lime"] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

    fruit["lime"] = "great with tequila"

    # used as with dictionaries for values() and items()
    # although this is clearly not a dict as can be seen by the two prints
    # of values() and items()
    for v in fruit.values():
        print(v)
    print(fruit.values())
    print("=" * 40)

    for f in fruit.items():
        print(f)
    print(fruit.items())
    print("=" * 40)

    # showcasing that the shelve behaves like a dictionary
    for snack in fruit:
        print(snack + ": " + fruit[snack])
    print("=" * 40)

    # the contents of the shelve are not necessarily sorted
    ordered_keys = list(fruit.keys())
    ordered_keys.sort()
    for f in ordered_keys:
        print(f + " - " + fruit[f])
    print("=" * 40)

    # demonstrating the use of 'get' to deal with non-existing keys
    while True:
        dict_key = input("Please enter a fruit: ")
        if dict_key == "quit":
            break

        # using get the code is only a one-liner
        description = fruit.get(key=dict_key, default="We don't have a {}".format(dict_key))

        # instead of using 'get' we can check if the key exists
        if dict_key in fruit:
            description = fruit[dict_key]
        else:
            print("We don't have a {}".format(dict_key))
        print(description)

print(fruit)
