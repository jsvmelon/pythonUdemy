print("Please enter three numbers separated by ',' :", end="")
value_string = input()
values = value_string.split(",")
print(int(values[0]) + int(values[1]) - int(values[2]))
