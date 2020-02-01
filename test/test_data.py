import ugapi
from ugapi import wiki


def test_data():
    tabs = ugapi.get_from_search("dream theater")
    assert len(tabs) > 0


# def test_wiki_search():
#     songs = wiki.get_songs_from_album("When Dream and Day Unite")
#     assert len(songs) == 8, "There should be 8 tracks on the album"


# def test_wiki_should_find_albums():
#     songs = wiki.get_songs_from_album("Dream Theater 2013")
#     assert len(songs) == 10, "There should be 10 tracks on the album"
