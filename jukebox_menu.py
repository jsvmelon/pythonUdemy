from lists.album_data import albums


def choose_album():
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    return int(input()) - 1  # return 0 based result


# int album_choice_input
def choose_song(album_choice_input):
    print("Please choose your song (invalid choice exits):")
    for index, (track_number, song) in enumerate(albums[album_choice_input][SONGS_LIST_INDEX]):
        print("{}: {}".format(track_number, song))

    return int(input()) - 1  # return 0 based result


SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

album_choice = 0  # this is just an initialisation - the value is never used
while 0 <= album_choice < len(albums):
    album_choice = choose_album()
    if 0 <= album_choice < len(albums):
        song_choice = choose_song(album_choice)
        if 0 <= song_choice < len(albums[album_choice][SONGS_LIST_INDEX]):
            print("Playing {} ...\n".format(albums[album_choice][SONGS_LIST_INDEX][song_choice][SONG_TITLE_INDEX]))
