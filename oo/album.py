from typing import List

from song import Song


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist_name (Artist): The artist responsible for the album. If not specified,
        the artist will default to and artist with the name "Various Artists"
        tracks (List[Song]): A list of songs of the album

    Methods:
        add_song: Use to add a new song to the album's track list
    """

    def __init__(self, name: str, year: int, artist_name: str = "Various Artists"):
        self.name: str = name
        self.year: int = year
        self.artist: str = artist_name
        self.tracks: List[Song] = []

    def add_song(self, song: Song, position: int = None) -> None:
        """Adds a song to the track list

        :param song: A song to add
        :param position: If specified, the song will be added to that position
        in the track list - inserting between other songs if necessary.
        Otherwise, the song will be added to the end of the list.
        """

        if position is None:
            position = len(self.tracks)

        for index, song_entry in enumerate(self.tracks):
            if song_entry.title == song.title:
                if index != position:
                    # the object is present but at the wrong position
                    self.tracks.remove(song_entry)
                    self.tracks.insert(position, song)
                return None

        # the song is not present in the tracks list
        self.tracks.insert(position, song)
