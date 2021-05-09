low = 1
high = 1000
guesses = 1

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

while True:
    guess = low + (high-low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct ".
                     format(guess)).casefold()

    if high_low == "h":
        # guess higher
        low = guess + 1
        guesses += 1
    elif high_low == "l":
        # guess lower
        high = guess - 1
        guesses += 1
    elif high_low == "c":
        # correct guess
        print("yay! Got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c")
