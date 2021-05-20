a = b = c = d = e = f = 12
print(c)

# the right hand side is a tuple !
x, y, z = 1, 2, 76
print(x, y, z)

print("Unpacking a tuple")

data = 1, 2, 76
x, y, z = data
print(x, y, z)

# works also with other sequence types
data = [1, 2, 76]
x, y, z = data
print(x, y, z)
