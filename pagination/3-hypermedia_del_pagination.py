#!/usr/bin/env python3
"""
3. Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    # ... [rest of the Server class]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page with deletion-resilient hypermedia pagination.

        Parameters:
        index (int): The current start index of the return page.
        page_size (int): The size of the page.

        Returns:
        Dict: A dictionary with pagination information and the data.
        """
        assert index is None or (
           isinstance(index, int) and 0 <= index < len(self.__indexed_dataset))

        if index is None:
            index = 0

        data = []
        next_index = index
        dataset = self.indexed_dataset()

        while len(data) < page_size and next_index < len(dataset):
            item = dataset.get(next_index, None)
            if item is not None:
                data.append(item)
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }


# Example usage
server = Server()
print(server.get_hyper_index(0, 10))
