def read_integer():
    """
    Reads an `integer` from the command line and returns the value.
    If the input is non-numerical the user is requested to enter their data
    until they provide valid input.
    The function allows for a negative value to be entered.
    :return: The numerical value entered by the user
    """
    value = ""
    while not value.isnumeric():
        value = input()

        # cover the case of a negative value
        if len(value) > 0 and value[0] == "-" and value[1:].isnumeric():
            return int(value)

        # normal positive integer
        elif value.isnumeric():
            return int(value)
        else:
            print("Please enter a numeric value")


answer = 5

print("Please guess a number (1-10)")
# guess = int(input())
guess = read_integer()

if guess == answer:
    print("Well done on the first guess")
else:
    if guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")

    # try again
    guess = read_integer()
    if guess != answer:
        print("Wrong again :-(")
    else:
        print("Well done on the second guess")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed right")
#     else:
#         print("Wrong again :-(")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed right")
#     else:
#         print("Wrong again :-(")
# else:
#     print("Awesome, you guessed right")
