from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from wikia_champions.items import WikiaChampionsList
from wikia_champions.items import WikiaChampionsHomepage
from wikia_champions.items import WikiaChampionsBackground
from wikia_champions.items import WikiaChampionsStrategy
from wikia_champions.items import WikiaChampionsSkinsTrivia
import json
#from pprint import pprint

class ChampsSpider(BaseSpider):
    name = "champs"
    allowed_domains = ["wikia.com"]
    start_urls = [
        "http://leagueoflegends.wikia.com/wiki/List_of_champions"
    ]
    
    def parse(self,response):
        sel = Selector(response)
        #get relativeURLs
        relativeURLs = sel.xpath('//td/span[@class="character_icon"]/a/@href').extract()
        #save baseURL
        baseURL = get_base_url(response)
        #output each champion's URL
        for relativeURL in relativeURLs:
            item = WikiaChampionsList()
            item['champ_url'] = urljoin_rfc(baseURL,relativeURL)
            yield item
            
            
class ChampHomepageSpider(BaseSpider):
    name = "champsHomepage"

    def __init__(self, filename=None):
        if filename:
            json_data = open(filename)
            data = json.load(json_data)
            for i in data:
                self.start_urls.append(i["champ_url"].encode("utf-8"))  

    allowed_domains = ["wikia.com"]
    
    start_urls = []
    
    def parse(self,response):
        sel = Selector(response)
        item = WikiaChampionsHomepage()
        item['url'] = get_base_url(response)
        item['urldoc'] = sel.xpath('//td/span/text()').extract() + sel.xpath('//p/text()').extract()
        yield item
 
class ChampBackgroundSpider(BaseSpider):
    name = "champsBackground"

    def __init__(self, filename=None):
        if filename:
            json_data = open(filename)
            data = json.load(json_data)
            for i in data:
                self.start_urls.append(i["champ_url"].encode("utf-8")+"/Background")  

    allowed_domains = ["wikia.com"]
    
    start_urls = []
    
    def parse(self,response):
        sel = Selector(response)
        item = WikiaChampionsBackground()
        item['url'] = get_base_url(response)
        item['urldoc'] = sel.xpath('//div[@class="mw-content-ltr"]/p/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/p/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/a/text()').extract()+sel.xpath('//blockquote[@class="quote"]/div/text()').extract()+sel.xpath('//i/text()').extract()
        yield item

class ChampStrategySpider(BaseSpider):
    name = "champsStrategy"

    def __init__(self, filename=None):
        if filename:
            json_data = open(filename)
            data = json.load(json_data)
            for i in data:
                self.start_urls.append(i["champ_url"].encode("utf-8")+"/Strategy")  

    allowed_domains = ["wikia.com"]
    
    start_urls = []
    
    def parse(self,response):
        sel = Selector(response)
        item = WikiaChampionsStrategy()
        item['url'] = get_base_url(response)
        item['urldoc'] = sel.xpath('//div[@class="mw-content-ltr"]/ul/li/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/span/a/span/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/h2/span/text()').extract()
        yield item  
        
class ChampSkinsTrivia(BaseSpider):
    name = "champsSkinsTrivia"

    def __init__(self, filename=None):
        if filename:
            json_data = open(filename)
            data = json.load(json_data)
            for i in data:
                self.start_urls.append(i["champ_url"].encode("utf-8")+"/SkinsTrivia")  

    allowed_domains = ["wikia.com"]
    
    start_urls = []
    
    def parse(self,response):
        sel = Selector(response)
        item = WikiaChampionsSkinsTrivia()
        item['url'] = get_base_url(response)
        item['urldoc'] = sel.xpath('//div[@class="mw-content-ltr"]/ul/li/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/h2/span/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/span/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/ul/li/span/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/i/span/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/span/a/span/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/span/span/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/ul/li/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/b/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/ul/li/b/a/text()').extract()+sel.xpath('//div[@class="mw-content-ltr"]/ul/li/ul/li/span/a/span/text()').extract()
        yield item         