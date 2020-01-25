from .TabEngine import tab_engine

__version__ = "v0.1.0"


def get_from_search(title, **kwargs):
    return tab_engine.process(title=title, **kwargs)
