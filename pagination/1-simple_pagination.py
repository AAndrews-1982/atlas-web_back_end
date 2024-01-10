#!/usr/bin/env python3
"""1. Simple pagination"""

import csv
from typing import List


def index_range(page, page_size):
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
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        pages = []

        if start_index >= len(self.dataset()):
            return pages

        pages = self.dataset()
        return pages[start_index:end_index]

# Example usage
# server = Server()
# print(server.get_page(1, 10))
