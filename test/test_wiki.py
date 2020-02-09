import os
import re
import ugapi


def test_wiki_search():
    albums = [
        "When Dream and Day Unite",
        "Awake"
    ]
    for album in albums:
        ugapi.get_songs(album)

    for album in albums:
        album_path = f"{re.sub('[^A-Za-z0-9]+', '_', album)}.csv"
        assert os.path.exists(album_path), "Export didn't work"
        os.remove(album_path)


# def test_wiki_should_find_albums():
#     songs = wiki.get_songs_from_album("Dream Theater 2013")
#     assert len(songs) == 10, "There should be 10 tracks on the album"
