menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
#
# print(meals)
#
# # meals = [meal for meal in menu if "spam" not in meal]
# meals = [
#     meal if "spam" not in meal else "a meal was skipped"  # expression
#     for meal in menu  # iterations
# ]
#
# print(meals)
#
# x = 12
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)

for meal in menu:
    print(meal,
          "contains chicken" if "chicken" in meal else "contains bacon"
          if "bacon" in meal else "contains egg")

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)

print(items)
print()

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break

# play fizzbuzz challenge
fizzbuzz = [
    "fizzbuzz" if number % 15 == 0 else
    ("fizz" if number % 3 == 0 else
     ("buzz" if number % 5 == 0 else str(number)))
    for number in range(1, 100)
]
print(fizzbuzz)
