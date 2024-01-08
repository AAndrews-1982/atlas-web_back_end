#!/usr/bin/env python3
"""1. Simple pagination"""

import csv


def index_range(page: int, page_size: int) -> tuple:

    """
    Calculate the start and end index for a page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    def __init__(self, dataset: str):
        self.__dataset = dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> list:
        """
        Get a page from the dataset.

        Parameters:
        page (int): The page number.
        page_size (int): The number of items per page.

        Returns:
        list: The list of items on the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        page_data = []
        with open(self.__dataset, mode='r', encoding='utf-8') as csvfile:
            data_reader = csv.reader(csvfile)
            for i, row in enumerate(data_reader):
                if i >= start_index and i < end_index:
                    page_data.append(row)

        return page_data


# Example usage
server = Server('Popular_Baby_Names.csv')
print(server.get_page(1, 10))
