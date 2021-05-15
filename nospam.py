menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# approach 1, just printing the menu item in each meal that are not spam
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ")
    print()

# approach 2, remove spam item from each meal
for meal in menu:
    top_index = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        if item == "spam":
            del meal[top_index - index]
    print(meal)

