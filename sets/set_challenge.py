vowels: frozenset = frozenset("aeiou")

text = input("Enter some text: ")
text_as_set = set(text)

# using sets
consonants_sorted = sorted(text_as_set.difference(vowels))
print(consonants_sorted)

# if we want duplicate consonants we can't use a set as the result
for vowel in vowels:
    text = text.replace(vowel, "")
print(text)
