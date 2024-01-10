#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""
import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary for deletion-resilient hypermedia pagination."""
        assert isinstance(index, int) and isinstance(page_size, int)
        assert index is None or 0 <= index < len(self.__indexed_dataset)

        data: List[List] = []
        next_index = index if index is not None else 0
        current_index = next_index

        while len(data) < page_size and current_index < len(
                self.__indexed_dataset):
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
                next_index = current_index + 1
            current_index += 1

        return {
            'index': index if index is not None else 0,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
