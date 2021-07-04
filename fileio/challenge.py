with open("./sample_copy.txt", mode='a') as file:
    for number in range(2, 13):
        for multiplier in range(2, 13):
            print("{0:2} times {1} is {2}".format(multiplier, number, multiplier * number), file=file)
        print("-" * 40, file=file)
