empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
sorted_numbers = (sorted(numbers))

print(numbers)
print(sorted_numbers)

digits = list("41243241345688566")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()

print(more_numbers)

print((numbers is more_numbers))
print(numbers == more_numbers)

# even.extend(odd)
# another_even = even
# even.sort(reverse=True)
# print(even)
# print(another_even)
#
# print(min(even), max(even))
#
# print(min(odd), max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("iss"))
#
# even.append(10)
# print(even)
