parrot = "Norwegian Blue"

letter = input("Enter a character: ")
if letter.casefold() in parrot.casefold():
    print("Letter {} is in {}".format(letter, parrot))

if letter.casefold() not in parrot.casefold():
    print("Letter {} is not in {}.".format(letter, parrot))

