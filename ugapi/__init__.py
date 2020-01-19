from .TabEngine import tab_engine
import pandas as pd


def get_from_search(title):
    tabs = tab_engine.process(title=title)
    assert len(tabs) > 0
