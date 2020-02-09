import re
import json
import scrapy
import pandas as pd


class WikiSpider(scrapy.Spider):
    name = "tabs"
    album_name = None
    songs = pd.DataFrame()

    def parse(self, response):
        headers = (
            response
            .xpath("//table")
            .css(".tracklist")[0]
            .xpath("*/tr[descendant::th and count(child::*)>2]")
            .xpath("th//text()")
            .getall()
        )

        content = (
            response
            .xpath("//table")
            .css(".tracklist")
            .xpath("*/tr[descendant::td]")
        )
        c = [
            [
                ''.join(
                    t.xpath("descendant-or-self::*/text()").getall()
                ) for t in row.xpath("td")
            ] for row in content if len(row.xpath("td")) == len(headers)
        ]
        self.album_name = re.sub('[^A-Za-z0-9]+', '_', self.album_name)
        pd.DataFrame(c, columns=headers).to_csv(f'{self.album_name}.csv')
