from .TabEngine import tab_engine


def get_from_search(title, **kwargs):
    return tab_engine.process(title=title, **kwargs)
