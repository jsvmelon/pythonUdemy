choice = None
options = ["1: one", "2: two", "3: three", "4: four", "0: exit"]
while choice != 0:
    if choice not in range(1, 5):
        # print the option menu
        print("Choose one from the following options")
        for option in options:
            print(option)

    choice = int(input())

    if choice in range(1, 5):
        print("You chose option {}".format(choice))
