#!/usr/bin/env python3
"""Module providing a helper function for pagination index calculation."""
from typing import Tuple


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
