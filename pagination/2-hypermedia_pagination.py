#!/usr/bin/env python3
"""2. Hypermedia pagination"""

import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for
    a given page and page size.

    This function is used to determine the range
    of records to return from a dataset for pagination purposes.

    Parameters:
    page (int): The current page number in the pagination sequence.
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing two integers, representing the start
    index and the end index for the page within the dataset.
    """
    start_index = (page - 1) * page_size
    return start_index, start_index + page_size


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve and cache the dataset from a CSV file.

        This function reads the dataset from a CSV file,
        caches it in memory, and returns it. The dataset is stored
        in a private variable and read from the file only once.
        Subsequent calls return the cached data.

        Returns:
        List[List]: A list of lists where each inner list represents a
        row of data from the dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        pages = []

        if start_index >= len(self.dataset()):
            return pages

        pages = self.dataset()
        return pages[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a page with hypermedia information from the dataset.

        Returns:
        Dict: A dictionary with pagination details.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper
