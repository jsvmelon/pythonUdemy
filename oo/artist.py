from typing import List
from album import Album


class Artist:
    """Basic class to store artist details"""

    def __init__(self, name: str = "Various Artists") -> None:
        """Initialisation
        
        :param name: Name of the artist (optional). If no name is given the name is set to "Various Artists"
        """
        self.name: str = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> Album:
        """Add a new album to the list

        :rtype: None
        :param album: The album to be appended. If the album is already present it will not be
        added again.
        :return If the album was not present in the list already the album is returned.
        Otherwise, the album from the list is returned instead.
        """
        for album_in_list in self.albums:
            if album.name == album_in_list.name:
                return album_in_list

        self.albums.append(album)
        return album
