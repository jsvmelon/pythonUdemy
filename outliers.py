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
    del data[stop+1:]
    print("After: {}".format(data))
    return data


# this is the first variant of deleting outliers which produces problems with
# the index in the loop
def erroneous_delete(data):
    print("Before: {}".format(data))

    del data[0:2]
    print("Delete first bit: {}".format(data))

    # this does not work
    for index, value in enumerate(data):
        if not (get_min_valid() < value < get_max_valid()):
            del data[index]

    print("After: {}".format(data))
    return data


# traverse the list backwards, then we can delete each index in place
# this then also works if the list is not sorted
def second_improvement(data):
    print("Before: {}".format(data))
    for i in range(len(data) - 1, -1, -1):
        if not (get_min_valid() < data[i] < get_max_valid()):
            del data[i]
    print("After: {}".format(data))
    return data


def test_with_data(test_function):
    input_data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186,
                  187, 188, 191, 350, 360]
    expected_result = [104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186,
                       187, 188, 191]
    modified_data = test_function(input_data)
    if modified_data == expected_result:
        return True
    else:
        return False


print("Erroneous delete")
erroneous_delete(get_data())

print("\nWorks, but clumsily")
first_improvement(get_data())

print("\nThis should be better")
second_improvement(get_data())

print(test_with_data(erroneous_delete))
print(test_with_data(first_improvement))
print(test_with_data(second_improvement))
