locations = {
    0: "in front of the computer learning python",
    1: "building",
    2: "hill",
    3: "inside well house",
    4: "in a valley",
    5: "forest",
}

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
QUIT = "Q"

d = {
    NORTH: ["N", "NORTH", "GO NORTH"],
    SOUTH: ["S", "SOUTH", "GO SOUTH"],
    WEST: ["W", "WEST", "GO WEST"],
    EAST: ["E", "EAST", "GO EAST"],
    QUIT: ["Q", "QUIT", "AHHH"],
}

# dictionary of allowed commands mapping to one of the direction keys
commands = {}
for direction in d:
    for alternative in d[direction]:
        commands[alternative] = direction
print(commands)

available_paths = {
    0: {QUIT: 0},
    1: {WEST: 2, EAST: 3, NORTH: 5, SOUTH: 4, QUIT: 0},
    2: {NORTH: 5, QUIT: 0},
    3: {WEST: 1, QUIT: 0},
    4: {NORTH: 1, WEST: 2, QUIT: 0},
    5: {WEST: 2, SOUTH: 1, QUIT: 0}
}

current_location = 1
# print(", ".join(exits[current_location]))

while current_location != 0:
    print("you are at " + locations[current_location])

    direction = input("Available paths are "
                      + ", ".join(available_paths[current_location])
                      + " ").upper()

    direction = commands[direction] if direction in commands else ""

    print()
    if direction in available_paths[current_location]:
        current_location = available_paths[current_location][direction]
    else:
        print("You cannot go in that direction\n")

else:
    print(locations[current_location])
