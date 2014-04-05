from scrapy.contrib.spiders import SitemapSpider
from scrape.items import ScrapeItem
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url

class WikiaFinal(SitemapSpider):
    sitemap_urls = ['http://leagueoflegends.wikia.com/sitemap-index.xml']
    sitemap_follow = ['/sitemap-leagueoflegends-NS_0-0','/sitemap-leagueoflegends-NS_0-1']
    name = 'wikialol'

    def parse(self, response):
        print response.url
        return

class ChampHomepageSpider(BaseSpider):
    name = "urlcontent"

    def __init__(self, filename=None):
        if filename:
            data = open(filename).read().split("\n")
            for i in data:
                self.start_urls.append(i)  

    allowed_domains = ["wikia.com"]
    
    start_urls = []
    
    def parse(self,response):
        sel = Selector(response)
        item = ScrapeItem()
        item['url'] = get_base_url(response)

        item['urldoc'] = sel.xpath('//text()[not(ancestor::script)][not(ancestor::style)][not(ancestor::form)]').extract() #get all the text except script, style, or form
        yield item