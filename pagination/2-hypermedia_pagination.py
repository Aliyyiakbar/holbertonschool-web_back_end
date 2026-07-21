#!/usr/bin/env python3
"""Module providing hypermedia pagination of popular baby names."""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for a given page and page size.

    Page numbers are 1-indexed, meaning the first page is page 1. The returned
    tuple contains the start index (inclusive) and end index (exclusive) that
    correspond to the range of items to return in a list for the given
    pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset as a list of rows.

        Uses assert to verify that both page and page_size are integers
        greater than 0. Uses index_range to find the correct indexes to
        paginate the dataset. If the input arguments are out of range for
        the dataset, an empty list is returned.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary with hypermedia metadata for the given page.

        The dictionary contains the page_size (length of the returned dataset
        page), the current page number, the dataset page itself, the next page
        number (or None if there is no next page), the previous page number
        (or None if there is no previous page), and the total number of pages
        in the dataset as an integer.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
