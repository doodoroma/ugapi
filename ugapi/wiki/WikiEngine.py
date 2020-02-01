import logging
import wikipedia
from scrapy.crawler import CrawlerProcess
from .WikiSpider import WikiSpider
from .WikiPipeline import SongsPipeline


class WikiEngine():

    def __init__(self):
        self.log = logging.getLogger(__name__)
        super().__init__()

    def process(self, title, save_to=None):
        return self._process(
            self._construct_url(title=title),
            save_to=save_to
        )

    def _process(self, url, save_to=None):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'ITEM_PIPELINES': {
                'ugapi.wiki.WikiPipeline.SongsPipeline': 300
            }
        })
        process.crawl(WikiSpider, start_urls=[
            url
        ])
        process.start()
        if save_to is not None:
            self.log.info(f'Data will be saved to {save_to}')
            SongsPipeline.songs.to_csv(save_to)

        return SongsPipeline.songs

    def _construct_url(self, title=None):
        best_page_title = wikipedia.search(f'{title} (album)')[0]
        return wikipedia.page(best_page_title).url


wiki_engine = WikiEngine()
