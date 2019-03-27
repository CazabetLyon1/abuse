import scrapy
from abuse.items import AbuseItem
from scrapy.loader import ItemLoader

class abuseSpider(scrapy.Spider):
    name = 'bcabuse'
    start_urls = ['https://www.bitcoinabuse.com/reports']

    def parse(self,response):
        for key in response.xpath("//div[@class='col-xl-4 col-md-6 mb-3']"):
            l = ItemLoader(item=AbuseItem() , selector=key)
            l.add_xpath('key',".//a")
            yield l.load_item()


        #callback pour appeler parser au page suivant
        next_page = response.xpath("//ul[@class='pagination']/li/a[@rel='next']/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)
