cities = ["Adelaide", "Alice Springs", "Darwin", "Mebourne", "Sydney"]

with open("write.txt", mode='w') as city_file:
    for city in cities:
        print(city, file=city_file)

# test what we have written into the file by reading it
cities = []
with open("write.txt", mode='r') as city_file:
    for city in city_file:
        cities.append(city.strip("\n"))

print(cities)
for city in cities:
    print(city)

# some things can be written but not read back
imelda = (
    "More Mayhem", "Imelda May", "2011",
    ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
)

with open("../imelda.txt", mode="w") as imelda_file:
    print(imelda, file=imelda_file)

# using eval to read the data back in a set
with open("../imelda.txt", mode='r') as imelda_file:
    contents = imelda_file.readline()

# eval is not great for security reasons in case the data has been modified
# and malicious code has been introduced
imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
