import scrapy


class PepParseItem(scrapy.Item):
    """Представляет один элемент списка документации PEP."""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
