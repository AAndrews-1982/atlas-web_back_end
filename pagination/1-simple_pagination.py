#!/usr/bin/env python3
"""1. Simple pagination"""

import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a page and page size.
    """
    start_index = (page - 1) * page_size
    return start_index, start_index + page_size


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                self.__dataset = list(csv.reader(f))[1:]  # Skip header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        Parameters:
        page (int): The page number. Must be a positive integer.
        page_size (int): The number of items per page.
        Must be a positive integer.

        Returns:
        List[List]: The list of items on the requested page.
        Returns an empty list if the page is out of range.

        Raises:
        AssertionError: If `page` or `page_size` is
        not a positive integer.
        """
        assert isinstance(page, int) and page > 0,
        "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0,
        "Page size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:min(end_index, len(self.dataset()))]
