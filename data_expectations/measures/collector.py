import datetime
from .measures import Measures
from .internals import BloomFilter

BLOOM_FILTER_SIZE = 5000000
BLOOM_FILTER_FALSE_POSITIVE_RATE = 0.0005


class MeasuresCollector(object):
    def __init__(self):
        self.counter = 0
        self.collector = {}
        self.bloom = BloomFilter(BLOOM_FILTER_SIZE, BLOOM_FILTER_FALSE_POSITIVE_RATE)

    def add(self, row):
        for k, v in row.items():
            collector = self.collector.get(k, Measures())
            collector.count += 1

            if v is None:
                collector.missing += 1
                continue

            value_type = type(v)
            if value_type in (int, float, str, datetime.date, datetime.datetime):
                collector.maximum = max(v, collector.maximum or v)
                collector.minimum = min(v, collector.minimum or v)
            if value_type in (int, float):
                collector.cummulative_sum += v

            v = str(v)
            if self.bloom.add(v):
                collector.unqiue_items += 1

            if collector.unqiue_items <= 25:
                collector.unique_list[v] = collector.unique_list.get(v, 0) + 1

            self.collector[k] = collector
