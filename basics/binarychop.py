low = 1
high = 1000
guesses = 0

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

while low != high:
    guesses += 1
    guess = low + (high - low) // 2
    user_feedback = input("My guess is {}. Should I guess higher or lower? "
                          "Enter h or l, or c if my guess was correct ".
                          format(guess)).casefold()

    if user_feedback == "h":
        # guess higher
        low = guess + 1
    elif user_feedback == "l":
        # guess lower
        high = guess - 1
    elif user_feedback == "c":
        # correct guess
        print("yay! Got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c")
else:
    print("you thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
