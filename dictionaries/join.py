myList = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"

newString = ""
for c in myList:
    newString += c + ", "
print(newString)

newString = ", ".join(myList)
print(newString)

newString = ", ".join(letters)
print(newString)

locations = {
    0: "in front of the computer learning python",
    1: "building",
    2: "hill",
    3: "inside well house",
    4: "in a valley",
    5: "forest",
}

exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]

current_location = 1
# print(", ".join(exits[current_location]))

while True:
    print(locations[current_location])

    available_exits = ", ".join(exits[current_location])

    if current_location == 0:
        break

    direction = input("Available exits are " + available_exits + " ").upper()
    print()
    if direction in exits[current_location]:
        current_location = exits[current_location][direction]
    else:
        print("You cannot go in that direction")
