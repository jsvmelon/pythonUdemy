text = "What have the romans ever done for us?"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(" ")]
print(words)

lc_words = text.split(" ")  # no need for a comprehension
print(lc_words)

lc_words = [word for word in text.split(" ")]  # don't do this - it is unnecessary
print(lc_words)

