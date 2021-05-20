t = "a", "b", "c"
print(t)

s = ("a", "b", "c")
print(s)

# tuples are immutable - the next line does not work
# s[0] = "fff"

print("Hello", ("five", "seven", "whatever"))

print(t[0], t[1], t[2])

t2 = list(t)
print(t2)

# list is mutable
t2[0] = "fff"

first, second, third = t
print(first)
print(second)
print(third)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

# using unpacking we can work with names instead
name, length, width, height, price = table
print(length * width)

