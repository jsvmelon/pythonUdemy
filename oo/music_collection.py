from typing import List
from album import Album
from artist import Artist
from song import Song


class MusicCollection:

    def __init__(self):
        self.artist_list: List[Artist] = []

    def load_data(self):

        with open("albums.txt", "r") as albums:
            for line in albums:
                # get the data line
                artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
                year_field = int(year_field)

                # add the new artist to the list
                new_artist = self.add_to_artist_list(artist_field)

                # create the basic objects from the data
                new_song = Song(song_field, artist_field)
                new_album = Album(album_field, year_field, artist_field)

                # create the cross connections
                new_album = new_artist.add_album(new_album)
                new_album.add_song(new_song)
                print("Processed ... ", artist_field, album_field, year_field, song_field)

    def add_to_artist_list(self, artist_name: str) -> Artist:
        """Function to create a new artist and add them to the list if they are not present yet.
        In addition the function returns either the newly created and added artist object or the artist corresponding to
        the artist_name parameter.

        :param artist_name: the name of the artist to be retrieved or added
        :return the artist sought or a newly created artist object
        """
        # first check if we have the artist already in the list
        for artist in self.artist_list:
            if artist.name == artist_name:
                print("Artist {} found in list".format(artist_name))
                return artist

        # create a new artist object and add the new artist to the list
        new_artist = Artist(artist_name)
        self.artist_list.append(new_artist)
        print("Added artist {} to list".format(new_artist.name))
        return new_artist

    def create_checkfile(self):
        """Write the contents in a file for comparison with the input data"""
        with open("checkfile.txt", "w") as checkfile:
            for new_artist in self.artist_list:
                for new_album in new_artist.albums:
                    for new_song in new_album.tracks:
                        print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                              file=checkfile)


if __name__ == "__main__":
    collection = MusicCollection()
    collection.load_data()
    print(len(collection.artist_list))

    # for testing the data load
    collection.create_checkfile()
