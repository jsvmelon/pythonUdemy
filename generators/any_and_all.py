entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print("\nIterable with a 'False' value")
entries_with_zero = [1, 2, 3, 4, 5, 0]
print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))

print("=" * 80)
name = ""
if name:
    print("Hello {}".format(name))
else:
    print("Welcome stranger")

print("=" * 80)

# using an empty iterable
empty = []
print("all: {}".format(all(empty)))  # True
print("any: {}".format(any(empty)))  # False

# when combining the check for empty-ness of an iterable we need to use 'bool'
result = empty and all(entries)  # []
print(result)
result = bool(empty) and all(entries)  # False
print(result)
