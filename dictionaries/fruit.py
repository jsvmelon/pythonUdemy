fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {
    "cabbage": "favourite",
    "sprouts": "lovely",
    "spinach": "more fruit please"
}
print(veg)

# veg.update(fruit)
print(veg)

nice_and_nicer = fruit.copy()
nice_and_nicer.update(veg)
print(nice_and_nicer)
