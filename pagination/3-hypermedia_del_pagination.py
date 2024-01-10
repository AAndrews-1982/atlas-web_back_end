#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""
import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    FILE_PATH = "Popular_Baby_Names.csv"

    def __init__(self):
        self._data_cache = None
        self._data_indexed = None

    def load_data(self) -> List[List]:
        """Load and cache the dataset from CSV file."""
        if self._data_cache is None:
            with open(self.FILE_PATH) as file:
                csv_reader = csv.reader(file)
                self._data_cache = list(csv_reader)[1:]
        return self._data_cache

    def indexed_dataset(self) -> Dict[int, List]:
        """Create an indexed dataset for efficient retrieval."""
        if self._data_indexed is None:
            self._data_indexed = {
                i: row for i, row in enumerate(self.load_data())
            }
        return self._data_indexed

    def get_resilient_page(self, index: int = None,
                           page_size: int = 10) -> Dict:
        """Provide hypermedia pagination with resilience to deletion."""
        assert index is None or (isinstance(index, int) and
                                 0 <= index < len(self._data_indexed))
        assert isinstance(page_size, int) and page_size > 0

        page_data = []
        next_idx = index or 0
        current_idx = next_idx

        while len(page_data) < page_size and \
                current_idx < len(self._data_indexed):
            if current_idx in self._data_indexed:
                page_data.append(self._data_indexed[current_idx])
                next_idx = current_idx + 1
            current_idx += 1

        return {
            'index': index or 0,
            'next_index': next_idx,
            'page_size': len(page_data),
            'data': page_data
        }

# Example usage
# server = Server()
# print(server.get_resilient_page(0, 10))
