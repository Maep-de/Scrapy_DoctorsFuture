import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.deutsches-krankenhaus-verzeichnis.de/app/suche/bundesland/sachsen'
    ]

    def parse(self, response):
        for quote in response.css('div.tab-content'):
            yield {
                'Hospital': quote.css('div.tab-content strong a.tag::text').getall(),
                'text': quote.css('div.tab-content address::text').getall(),
            }


