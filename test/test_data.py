import ugapi


def test_data():
    tabs = ugapi.get_from_search("dream theater")
    assert len(tabs) > 0
