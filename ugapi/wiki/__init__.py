from .WikiEngine import wiki_engine


def get_songs_from_album(title, **kwargs):
    return wiki_engine.process(title=title, **kwargs)
