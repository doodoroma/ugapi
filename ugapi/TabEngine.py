import logging
from scrapy.crawler import CrawlerProcess
from .TabSpider import TabSpider
from .TabPipeline import TabPipeline
from .enums import TabType


class TabEngine():
    base_url = 'https://www.ultimate-guitar.com/'

    def __init__(self):
        self.log = logging.getLogger(__name__)
        super().__init__()

    def process(self, title, **kwargs):
        return self._process(
            self._construct_url(title=title),
            **kwargs
        )

    def _process(self, url, save_to=None):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'ITEM_PIPELINES': {
                'ugapi.TabPipeline.TabPipeline': 300
            }
        })
        process.crawl(TabSpider, start_urls=[
            url
        ])
        process.start()
        if save_to is not None:
            self.log.info(f'Data will be saved to {save_to}')
            TabPipeline.tabs.to_csv(save_to)

        return TabPipeline.tabs

    @property
    def _search_url(self):
        return f'{TabEngine.base_url}search.php'

    def _construct_url(self, title=None, order='title_srt', tab_type=TabType.TAB):
        url_arguments = '&'.join([
            f"title={title.replace(' ', '+')}",
            f"order={order}",
            f"type={tab_type}",
            f"page=1"
        ])
        return f'{self._search_url}?{url_arguments}'


tab_engine = TabEngine()
