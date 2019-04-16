import scrapy
from abuse.items import AbuseItem
from scrapy.loader import ItemLoader
import pandas as pd

link = "https://www.bitcoinabuse.com/reports/"


def extend_text(value):
    value2 = link + value
    return value2


def keys_restructure():
    keys = pd.read_csv(
        '/Users/khaled/Desktop/abuse/abuse/abuse/keys_reduced.csv', delimiter=',')
    tab_keys = keys.as_matrix()
    for i in range(len(tab_keys)):
        tab_keys[i] = extend_text(tab_keys[i])
    list = []
    for i in range(len(tab_keys)):
        list.append(tab_keys[i][0])
    return list


class reportSpider(scrapy.Spider):
    name = 'bcdata'
    ##
    start_urls = keys_restructure()

    def parse(self, response):
        i = 0
        for key in response.xpath("//table[@class='table table-striped table-bordered table-responsive-lg']/tbody"):
            # l = ItemLoader(item=AbuseItem() , selector=key)
            # l.add_xpath('key',".//i")
            # # yield l.load_item() .//table/tr[1]/
            while key.xpath(".//*").extract()[i] != None:
                yield{
                    'Address': key.xpath("//div[@class='card-body']/table/tr[1]/td/i").extract_first(),
                    'Deport_Count': key.xpath("//div[@class='card-body']/table/tr[2]/td").extract_first(),
                    'Last_Report': key.xpath("//div[@class='card-body']/table/tr[3]/td").extract_first(),
                    'Date': key.xpath(".//tr/td[1]").extract()[i],
                    'Abuse_Type': key.xpath(".//tr/td[2]").extract()[i],
                    'Abuser': key.xpath(".//tr/td[3]").extract()[i],
                    'Description': key.xpath(".//tr/td[4]").extract()[i]
                }
                i += 1
            i = 0
        # callback pour appeler parser au page suivant
        next_page = response.xpath(
            "//ul[@class='pagination']/li/a[@rel='next']/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
