# un-pickle data only from trusted sources - there are security problems
import pickle

imelda = (
    "More Mayhem", "Imelda May", "2011",
    ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(1346546, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

# load the data back
# have to read the data in the same order it was written
imelda = None
print(imelda)
with open("imelda.pickle", "rb") as pickle_file:
    imelda = pickle.load(pickle_file)
    even_list = pickle.load(pickle_file)
    odd_list = pickle.load(pickle_file)
    x = pickle.load(pickle_file)

print(imelda)

album, artist, year, track_list = imelda

print(album)
print(artist)
print(year)
print(track_list[2][1])

print("=" * 40)

for i in even_list:
    print(i)

for i in odd_list:
    print(i)

print(x)

# demonstration of the insecurity of un-pickling
pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")
