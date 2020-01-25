import ugapi
from ugapi.enums import TabType

tabs = ugapi.get_from_search(
    "dream theater", save_to='tabs.csv', tab_type=TabType.GUITAR_PRO
)
print(tabs.head())
