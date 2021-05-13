data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186, 187,
        188, 191, 350, 360]

min_valid = 100
max_valid = 200

# process the low values first
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

del data[:stop]
print(data)

stop = -1
while data[stop] >= max_valid:
    stop -= 1

print(stop)
del data[stop:]
print(data)

# del data[0:2]
# print(data)

#
# # this does not work
# for index, value in enumerate(data):
#     if not (min_valid < value < max_valid):
#         del data[index]
#
# print(data)
