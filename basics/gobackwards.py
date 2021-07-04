data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185,
        186, 187, 188, 191, 350, 360]
min_valid = 100
max_valid = 200

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)

