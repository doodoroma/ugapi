import ugapi
from ugapi import wiki
from ugapi.enums import TabType

# tabs = ugapi.get_from_search(
#     "dream theater", save_to='tabs.csv', tab_type=TabType.GUITAR_PRO
# )
# print(tabs.head())

songs = wiki.get_songs_from_album("Dream Theater 2013", save_to="dt.csv")
print(songs.head())
