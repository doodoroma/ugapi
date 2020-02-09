import logging
import wikipedia
import pandas as pd
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from ugapi.WikiSpider import WikiSpider

from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager

__version__ = "v0.1.6"


def _construct_url(title):
    best_page_title = wikipedia.search(f'{title} (album)')[0]
    return wikipedia.page(best_page_title).url


def _get_songs(album, **kwargs):
    crawler = CrawlerProcess(settings={'LOG_ENABLED': False})
    WikiSpider.album_name = album

    crawler.crawl(WikiSpider, start_urls=[
        _construct_url(album)
    ])

    crawler.start()


def get_songs(album):
    process = Process(target=_get_songs, args=(album,))
    process.start()
    process.join()
