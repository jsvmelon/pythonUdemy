import random


def get_data():
    return [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186, 187,
            188, 191, 350, 360]


def get_min_valid():
    return 100


def get_max_valid():
    return 200


# process the low values first
def first_improvement(data):
    print("Before: {}".format(data))
    if len(data) == 0:
        return data

    stop = 0
    for index, value in enumerate(data):
        if value >= get_min_valid():
            stop = index
            break

    del data[:stop]
    print("Intermediate: {}".format(data))

    stop = -1
    while data[stop] >= get_max_valid():
        stop -= 1

    print("Stop:", stop)
    del data[stop + 1:]
    print("After: {}".format(data))
    return data


# this is the first variant of deleting outliers which produces problems with
# the index in the loop
# THIS FUNCTION WORKS ONLY WITH SORTED DATA
def erroneous_delete(data):
    print("Before: {}".format(data))

    del data[0:2]
    print("Delete first bit: {}".format(data))

    # THIS DOES NOT WORK
    for index, value in enumerate(data):
        if not (get_min_valid() < value < get_max_valid()):
            del data[index]

    print("After: {}".format(data))
    return data


# traverse the list backwards, then we can delete each index in place
# this then also works if the list is not sorted
# THIS FUNCTION WORKS ONLY WITH SORTED DATA
def second_improvement(data):
    print("Before: {}".format(data))
    for i in range(len(data) - 1, -1, -1):
        if not (get_min_valid() <= data[i] <= get_max_valid()):
            del data[i]
    print("After: {}".format(data))
    return data


# This function produces a list of random integer data
# In addition the function returns the amount of good and bad data in
# in accordance with get_min_valid() and get_max_valid()
# The function returns a list of three results:
# - list of random integer data
# - number of good data points
# - number of bad data points
def data_generator():
    data = []
    good_data = 0
    bad_data = 0
    for i in range(0, random.randint(0, 100)):
        case = random.randint(0, 10)
        if case <= 8:
            data.extend([random.randint(get_min_valid(), get_max_valid())])
            good_data += 1
        elif case == 9:
            data.extend([random.randint(0, get_min_valid())])
            bad_data += 1
        else:
            data.extend([random.randint(get_max_valid() + 1, 1000)])
            bad_data += 1
    return [data, good_data, bad_data]


def test_with_example_data(test_function):
    input_data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186,
                  187, 188, 191, 350, 360]
    expected_result = [104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186,
                       187, 188, 191]
    modified_data = test_function(input_data)
    if modified_data == expected_result:
        return True
    else:
        return False


def test_random(test_function):
    dataset = data_generator()
    data = dataset[0]
    good = dataset[1]
    bad = dataset[2]
    modified_data = test_function(data.copy())
    print("original: {}".format(data))
    print("modified: {}".format(modified_data))

    for item in modified_data:
        if not (get_min_valid() <= item <= get_max_valid()):
            print("Invalid data: {}".format(item))
            return False

    if len(modified_data) != (len(data) - bad):
        print("List length is not correct.\n"
              "Modified length = {}\n"
              "Original length = {}\n"
              "Number of bad data = {}".
              format(len(modified_data), len(data), bad))
        return False
    return True


def edge_case_test(test_function):
    data1 = []
    expected1 = []
    data2 = [100, 101, 199, 200]
    expected2 = [100, 101, 199, 200]
    data3 = [-100, -200]
    expected3 = []
    result = True

    test = test_function(data1)
    if test != expected1:
        print("Empty list not handled properly")
        result = False

    test = test_function(data2)
    if test != expected2:
        print("Edge values not handled correctly.")
        result = False

    test = test_function(data3)
    if test != expected3:
        print("Negative values not handled correctly")
        result = False

    return result



print("First function")
print(test_with_example_data(erroneous_delete))
print(test_random(erroneous_delete))
print(edge_case_test(erroneous_delete))

print("\nSecond function")
print(test_with_example_data(first_improvement))
print(test_random(first_improvement))
print(edge_case_test(first_improvement))

print("\nThird function")
print(test_with_example_data(second_improvement))
print(test_random(second_improvement))
print(edge_case_test(second_improvement))

print("Erroneous delete")
erroneous_delete(get_data())

print("\nWorks, but clumsily")
first_improvement(get_data())

print("\nThis should be better")
second_improvement(get_data())



