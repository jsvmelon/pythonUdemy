name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Your are not old enough to vote")
    print("Please come back in {0} years".format(18-age))

if age < 18:
    print("Your are not old enough to vote")
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in the Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")


# for i in range(1, 5):
#     print(i)
#     for k in range(1,3):
#         print("{0}:{1}".format(i, k))
#
#         print(".")
# print("*" * 80)