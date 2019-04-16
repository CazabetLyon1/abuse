import scrapy
from abuse.items import AbuseItem
from scrapy.loader import ItemLoader
import pandas as pd
import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


link = "https://bitcoin-otc.com/viewgpg.php?nick="


def extend_text(value):
    value2 = link + str(value)
    return value2


def keys_restructure():
    keys = pd.read_csv(
        '/Users/khaled/Desktop/abuse/abuse/abuse/nicks.csv', delimiter=',')
    tab_keys = keys.as_matrix()
    for i in range(len(tab_keys)):
        tab_keys[i] = extend_text(tab_keys[i][0])
    list = []
    for i in range(len(tab_keys)):
        list.append(tab_keys[i][0])
    return list


class nicksdataSpider(scrapy.Spider):
    name = 'ndata'
    start_urls = keys_restructure()

    def parse(self, response):
        for key in response.xpath("//table[@class='datadisplay sortable']/tr[@class='odd']"):
            yield {
                'nickname': key.xpath(".//td[2]/a/text()").extract_first(),
                'date': key.xpath(".//td[3]/text()").extract_first(),
                'key': key.xpath(".//td[4]/text()").extract_first(),
                'fingerprint': key.xpath(".//td[5]/a/text()").extract_first(),
                'bitcoinaddress': cleanhtml(key.xpath(".//td[6]").extract_first()),
                'last_authed': key.xpath(".//td[7]/text()").extract_first(),
                'is_authed': key.xpath(".//td[8]/text()").extract_first()
            }
