import scrapy
from abuse.items import AbuseItem
from scrapy.loader import ItemLoader

class jokesSpider(scrapy.Spider):
    name = 'nicks'
    start_urls = ['https://bitcoin-otc.com/viewratings.php'] 

    def parse(self,response):
       for key in response.xpath("//table[@class='datadisplay sortable']/tr"):
            l = ItemLoader(item=AbuseItem() , selector=key)
            l.add_xpath('key',".//td[2]/a/@href")
            yield l.load_item()
           
         
"""
        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)
            //table[@class='datadisplay sortable']/tbody/tr/td[@class='nowrap']
            .//table[@class='datadisplay sortable']/tbody/tr/td[2]/a/@href 
"""