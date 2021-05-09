answer = 5

print("Please guess a number (1-10)")
guess = int(input())

if guess == answer:
    print("Well done on the first guess")
else:
    if guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")

    # try again
    guess = int(input())
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
