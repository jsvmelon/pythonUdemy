data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186, 187,
        188, 191, 350, 360]
# del data[0:2]
# print(data)

min_valid = 100
max_valid = 200

# this does not work
for index, value in enumerate(data):
    if not (min_valid < value < max_valid):
        del data[index]

print(data)
