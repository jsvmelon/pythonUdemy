import timeit
text = "What have the romans ever done for us?"


def capitals():
    return [char.upper() for char in text]


def map_capitals():
    """use map to do the same"""
    return list(map(str.upper, text))


def words():
    return [word.upper() for word in text.split(" ")]


def map_words():
    return list(map(str.upper, text.split(" ")))


# for x in map(str.upper, text.split(" ")):
#     print(x, end=" ")

if __name__ == "__main__":
    print(timeit.timeit(capitals))
    print(timeit.timeit(map_capitals))
    print(timeit.timeit(words))
    print(timeit.timeit(map_words))
