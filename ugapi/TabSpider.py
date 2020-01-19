import json
import scrapy


class TabSpider(scrapy.Spider):
    name = "tabs"

    def parse(self, response):
        data_text = response.css('.js-store::attr(data-content)').get()
        data = json.loads(
            data_text
        )

        yield {
            'data': data
        }

        pages = data['store']['page']['data']['pagination']
        current_page = pages['current']
        total_page = pages['total']
        if current_page < total_page:
            yield response.follow(response.url.replace(
                f'page={current_page}', f'page={current_page + 1}'
            ), callback=self.parse)
