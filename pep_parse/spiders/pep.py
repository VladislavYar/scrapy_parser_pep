import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Spider парсинга PEP документации(номер, название, статус)."""
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Отдает ссылки на детальные страницы PEP-документаций."""
        all_peps = response.css('section#numerical-index tbody tr td + td a')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит данные детальной страницы PEP-документации."""
        name = response.css('h1.page-title::text')
        number = name.re(r'[0-9]+')[0]
        data = {
            'number': number,
            'name': name.get().strip(),
            'status': response.css('dt:contains("Status") '
                                   '+ dd abbr::text').get().strip(),
        }
        yield PepParseItem(data)
