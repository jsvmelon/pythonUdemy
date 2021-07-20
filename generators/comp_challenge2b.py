import timeit

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


def variant1():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)

    for x in result:
        pass

    return result


def variant2():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)

    for x in result:
        pass

    return result


def variant3():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations)]

    for x in exits_to_destination_3:
        pass

    return exits_to_destination_3


def nested_gen():
    """Using a generator"""
    exits_to_destination_3 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations))

    for x in exits_to_destination_3:
        pass

    return exits_to_destination_3


print(variant1())
print(variant2())
print(variant3())

result1a = timeit.timeit(variant1, number=100000)
result1b = timeit.timeit(variant1, setup='gc.enable()', number=100000)
result2a = timeit.timeit(variant2, number=100000)
result2b = timeit.timeit(variant2, setup='gc.enable()', number=100000)
result3a = timeit.timeit(variant3, number=100000)
result3b = timeit.timeit(variant3, setup='gc.enable()', number=100000)
result4a = timeit.timeit(nested_gen, number=100000)
result4b = timeit.timeit(nested_gen, setup='gc.enable()', number=100000)

print("nested for loops: ", result1a, result1b)
print("List comprehension inside a for loop: ", result2a, result2b)
print("nested comprehension", result3a, result3b)
print("nested generator", result4a, result4b)
