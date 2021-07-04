from lists.album_data import albums

for name, artist, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}, Songs: {}".format(name, artist, year, songs))

print()

album = albums[3]
print(album)

songs = album[3]
print(songs)

song = songs[2]
print(song)

song_title = song[1]
print(song_title)

print(albums[3][3][2][1])

# Challenge

# the song "The Way I Choose"
print(albums[1][3][5][1])

# the year Nightflight was released
print(albums[2][2])

# track number of "Kentish Town Waltz"
print(albums[3][3][3][0])

# the tuple representing "Keeping a Rendezvous"
print(albums[2][3][1])
