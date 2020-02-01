import pandas as pd


class SongsPipeline(object):
    songs = pd.DataFrame()

    def open_spider(self, spider):
        SongsPipeline.tabs = pd.DataFrame()

    def process_item(self, item, spider):
        SongsPipeline.songs = SongsPipeline.songs.append(pd.DataFrame(
            item['content'], columns=item['headers'])
        )
