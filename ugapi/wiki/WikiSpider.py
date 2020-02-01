import json
import scrapy


class WikiSpider(scrapy.Spider):
    name = "tabs"

    def parse(self, response):
        headers = (
            response
            .xpath("//table")
            .css(".tracklist")[0]
            .xpath("*/tr[descendant::th]")
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

        yield {
            'content': c,
            'headers': headers
        }
