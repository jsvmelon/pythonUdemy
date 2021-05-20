panagram = """The quick brown
 fox jumps\tover the lazy dog"""
words = panagram.split()
print(words)

numbers = "9,223,123,46,3354,463,34455,33"
print(numbers.split(","))

separators = ",.;: "
values = "".join(char if char not in separators else " " for char in numbers).split()
print(values)

# mini challenge
integer_values = []
for i in values:
    integer_values.extend([int(i)])

print(integer_values)
