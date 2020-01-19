import pandas as pd


class TabPipeline(object):
    tabs = pd.DataFrame()

    def open_spider(self, spider):
        TabPipeline.tabs = pd.DataFrame()

    def process_item(self, item, spider):
        TabPipeline.tabs = TabPipeline.tabs.append(pd.DataFrame(
            item['data']['store']['page']['data']['results']
        ))
        # return item
