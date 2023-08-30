from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_FORMAT = 'csv'
DOMAIN_PARSE = 'peps.python.org'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

FEEDS = {
    f'results/pep_%(time)s.{FILE_FORMAT}': {
        'format': FILE_FORMAT,
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
