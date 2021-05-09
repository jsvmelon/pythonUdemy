parrot = "Norwegian Blue"

for character in parrot:
    print(character)
#
numbers = "1,234,432;234:345.345 567"
#numbers = input("Give me numbers: ")
separators = ""

for character in numbers:
    if not character.isnumeric():
        separators = separators + character

print(separators)

values = "".join(character if character not in separators else " " for character in numbers).split()
print(values)
print(sum([int(val) for val in values]))

#

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
capitals = ""
for c in quote:
    if c.isupper():
        capitals = capitals + c
print(capitals)