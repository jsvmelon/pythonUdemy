available_choices = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi"]
current_choice = -1
computer_parts = []

# print the menu
print("Please add options from the list below:")
for number, part in enumerate(available_choices):
    print("{}: {}".format(number+1, part))

while current_choice != 0:
    if 1 <= current_choice <= len(available_choices):
        print("Adding {}".format(available_choices[current_choice - 1]))
        computer_parts.append(available_choices[current_choice - 1])
        current_choice = -1
    else:
        current_choice = int(input())

print(computer_parts)
