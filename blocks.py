name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Your are not old enough to vote")


# for i in range(1, 5):
#     print(i)
#     for k in range(1,3):
#         print("{0}:{1}".format(i, k))
#
#         print(".")
# print("*" * 80)