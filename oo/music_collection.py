from typing import List
from album import Album
from artist import Artist
from song import Song


def load_data():
    artist_list: List[Artist] = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # get the data line
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)

            # create the basic objects from the data
            new_song = Song(song_field, artist_field)
            new_album = Album(album_field, year_field, artist_field)
            new_artist = Artist(artist_field)

            # add the new artist to the list
            new_artist = add_to_artist_list(artist_list, new_artist)

            # create the cross connections
            new_album = new_artist.add_album(new_album)
            new_album.add_song(new_song)
            print("Processed ... ", artist_field, album_field, year_field, song_field)

    return artist_list


def add_to_artist_list(artist_list, new_artist) -> Artist:
    # first check if we have the artist already in the list
    for artist in artist_list:
        if artist.name == new_artist.name:
            print("Artist {} found in list".format(new_artist.name))
            return artist

    # add the new artist to the list
    artist_list.append(new_artist)
    print("Added artist {} to list".format(new_artist.name))
    return new_artist


def create_checkfile(artist_list: List[Artist]):
    """Write the contents in a file for comparison with the input data"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print(len(artists))

    create_checkfile(artists)
