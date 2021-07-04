available_choices = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi", "dvd drive"]
current_choice = -1
computer_parts = []

while current_choice != 0:
    if 1 <= current_choice <= len(available_choices):
        chosen_item = available_choices[current_choice-1]
        if chosen_item in computer_parts:
            print("Removing {} from your list".format(chosen_item))
            computer_parts.remove(chosen_item)
        else:
            print("Adding {}".format(chosen_item))
            computer_parts.append(chosen_item)
    else:
        # print the menu
        print("Please add options from the list below:")
        for number, part in enumerate(available_choices):
            print("{}: {}".format(number+1, part))

    current_choice = int(input())

print(computer_parts)
