import csv
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DT_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        """Создаёт словарь для хранения данных по статусам."""
        self.summary_statuses = {
            'Active': 0, 'Accepted': 0,
            'Deferred': 0, 'Final': 0,
            'Provisional': 0, 'Rejected': 0,
            'Superseded': 0, 'Withdrawn': 0,
            'Draft': 0, 'Active': 0,
            'April Fool!': 0, 'Total': 0
        }

    def process_item(self, item, spider):
        """Подсчитывает кол-во статусов."""
        status = item['status']
        self.summary_statuses[status] += 1
        self.summary_statuses['Total'] += 1
        return item

    def close_spider(self, spider):
        """Сохраняет итоговые данные в файл."""
        date_now = dt.now().strftime(DT_FORMAT)
        filename = BASE_DIR / f'results/status_summary_{date_now}.csv'
        with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
            csvfile = csv.writer(csvfile)
            csvfile.writerow(('Статус', 'Количество'))
            for status, count in self.summary_statuses.items():
                csvfile.writerow((status, count))
