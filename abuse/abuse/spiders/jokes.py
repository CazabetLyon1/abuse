import scrapy
from abuse.items import JokesItem
from scrapy.loader import ItemLoader

class jokesSpider(scrapy.Spider):
    name = 'jokes'
    start_urls = ['http://www.laughfactory.com/jokes/family-jokes'] 

    def parse(self,response):
        for jokes in response.xpath("//div[@class='jokes']"):
            l = ItemLoader(item=JokesItem() , selector=jokes)
            l.add_xpath('joke_text',".//div[@class='joke-text']/p")
            yield l.load_item()

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)
