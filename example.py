import ugapi

tabs = ugapi.get_from_search("dream theater", save_to='tabs.csv')
print(tabs.head())
