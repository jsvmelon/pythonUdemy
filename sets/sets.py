# set creation - variant 1
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

# set creation variont 2
wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

# with set creation variant 1 it is impossible to create an empty set
empty_set = set()
empty_dict = {}

empty_set.add("a")
# empty_dict.add("a")

even, squares_tuple, squares = set(), (), set()


def setup():
    global even, squares_tuple, squares
    even = set(range(0, 40, 2))
    squares_tuple = (4, 6, 9, 16, 25)
    squares = set(squares_tuple)


# checkout some sample operations with sets
setup()
print("The even set: " + even)
print(len(even))
print("The squares set" + squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print("=" * 40)
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print("=" * 40)

# minus '-' versus .difference (difference in readability
setup()
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)

# update_difference example
setup()
print("-" * 40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

# symmetric even minus squares
setup()
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric even minus even")
print(sorted(squares.symmetric_difference(even)))

# discard vs remove
setup()
squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
try:
    squares.remove(8)  # raises an error because 8 does not exist
except KeyError:
    print("The item 8 is not a member of the set")

# issubset and issuperset
setup()
squares.discard(9)
squares.discard(25)
if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")

# frozen set
setup()
frozen_even = frozenset(range(0, 100, 2))
print(frozen_even)

