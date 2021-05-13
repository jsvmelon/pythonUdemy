even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
another_even = even
even.sort(reverse=True)
print(even)
print(another_even)

print(min(even), max(even))

print(min(odd), max(odd))

print()
print(len(even))
print(len(odd))

print()
print("mississippi".count("iss"))

even.append(10)
print(even)
