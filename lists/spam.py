menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("Meal {} has a spam score of {}".format(meal, meal.count("spam")))
