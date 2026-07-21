#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination of popular baby names."""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page of the dataset with metadata.

        The returned dictionary contains the current start index of the
        returned page, the actual page of data, the current page size, and
        the next index to query with. Rows removed between two queries are
        skipped so that the user does not miss any items when changing page.
        """
        indexed = self.indexed_dataset()
        total = len(self.dataset())
        assert index is not None and isinstance(index, int)
        assert 0 <= index < total
        assert isinstance(page_size, int) and page_size > 0
        data = []
        idx = index
        while len(data) < page_size and idx < total:
            if idx in indexed:
                data.append(indexed[idx])
            idx += 1
        next_index = idx if idx < total else None
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index,
        }
