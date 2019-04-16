import scrapy
from abuse.items import AbuseItem
from scrapy.loader import ItemLoader


class nicksSpider(scrapy.Spider):
    name = 'nicks'
    start_urls = ['https://bitcoin-otc.com/viewratings.php']

    def parse(self, response):
        for key in response.xpath("//table[@class='datadisplay sortable']/tr"):
            l = ItemLoader(item=AbuseItem(), selector=key)
            l.add_xpath('key', ".//td[2]/a")
            yield l.load_item()
