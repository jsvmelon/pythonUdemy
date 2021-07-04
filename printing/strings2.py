#                   1
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

print(parrot[-1:-15:-1])
print(parrot[-1::-1])
print(parrot[::-1])


# print(parrot[-4:-2])
# print(parrot[-4:12])

# print(parrot[0:6])  # slice up to but not including 6
# print(parrot[3:5])  # slice up to but not including 6
# print(parrot[0:9])  # slice up to but not including 6
# print(parrot[:9])  # slice up to but not including 6
#
# print(parrot[10:14])
# print(parrot[10:])
# print(parrot[:])

# print(parrot)
# print(parrot[3], "\n" + parrot[4], "\n" + parrot[9], "\n" + parrot[3], "\n" + parrot[6], "\n" + parrot[8])
# print()
# print(parrot[3-14], "\n" + parrot[4-14], "\n" + parrot[9-14], "\n" + parrot[3-14], "\n" + parrot[6-14], "\n" + parrot[8-14])
# print()
# print(parrot[-11], "\n" + parrot[-10], "\n" + parrot[-5], "\n" + parrot[-11], "\n" + parrot[-8], "\n" + parrot[-6])
