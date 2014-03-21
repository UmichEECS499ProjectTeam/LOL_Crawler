# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class WikiaChampionsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass
class WikiaChampionsList(Item):
    champ_url = Field()
    
class WikiaChampionsHomepage(Item):
    url = Field()
    urldoc = Field()
    
class WikiaChampionsBackground(Item):
    url = Field()
    urldoc = Field()

class WikiaChampionsStrategy(Item):
    url = Field()
    urldoc = Field()

class WikiaChampionsSkinsTrivia(Item):
    url = Field()
    urldoc = Field()