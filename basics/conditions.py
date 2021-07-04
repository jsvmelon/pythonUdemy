age = int(input("How old are you? "))

if 16 <= age <= 67:
    print("You are of working age")
else:
    print("You are not of working age")


print("-" * 80)

if age < 16 or age > 67:
    print("You are not of working age")
else:
    print("You are of working age")

print("-" * 80)

if age in range(16, 68):
    print("you are of working age")
else:
    print("You are not of working age")

for i in range(7, 101, 7):
    print(i)