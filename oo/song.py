class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist_name (oo.artist.Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title: str, artist_name: str, duration: int = 0) -> None:
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist_name (oo.artist.Artist): An Artist object representing the song's creator
            duration (Optional[int]: Initial value for the 'duration' attribute.
                Will default to zero if not specified.
        """
        self.title: str = title
        self.artist: str = artist_name
        self.duration: int = duration
