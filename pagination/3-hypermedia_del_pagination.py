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
                # Exclude header
                self._data_cache = list(csv_reader)[1:]
        return self._data_cache

    def index_data(self) -> Dict[int, List]:
        """Create an indexed dataset for efficient retrieval."""
        if self._data_indexed is None:
            data = self.load_data()
            self._data_indexed = {i: data[i] for i in range(len(data))}
        return self._data_indexed

    def get_resilient_page(self, start_idx: Optional[int] = None,
                           size: int = 10) -> Dict:
        """Provide hypermedia pagination with resilience to deletion."""
        assert start_idx is None or (
            isinstance(start_idx, int) and
            0 <= start_idx < len(self._data_indexed)
        )
        assert isinstance(size, int) and size > 0

        page_data = []
        next_idx = start_idx or 0
        current_idx = next_idx

        while len(page_data) < size and current_idx < len(self._data_indexed):
            if current_idx in self._data_indexed:
                page_data.append(self._data_indexed[current_idx])
                next_idx = current_idx + 1
            current_idx += 1

        return {
            'index': start_idx or 0,
            'next_index': next_idx,
            'page_size': len(page_data),
            'data': page_data
        }
