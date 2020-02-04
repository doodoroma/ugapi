import os
import ugapi


def test_wiki_search():
    ugapi.get_songs("When Dream and Day Unite")
    ugapi.get_songs("Awake")
    os.path.exists("When Dream and Day Unite.csv")
    os.path.exists("Awake.csv")


# def test_wiki_should_find_albums():
#     songs = wiki.get_songs_from_album("Dream Theater 2013")
#     assert len(songs) == 10, "There should be 10 tracks on the album"
