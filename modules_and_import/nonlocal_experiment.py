def first():
    print("doing something")
    counter = 0

    def inner(my_counter):
        # nonlocal counter
        for i in range(1, 5):
            my_counter += 1
        return my_counter

    for k in range(1, 10):
        counter = inner(counter)
        print(counter)


first()
