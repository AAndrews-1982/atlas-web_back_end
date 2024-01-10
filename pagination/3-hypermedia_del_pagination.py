#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

# Additional blank line added before the function to resolve E302
def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    """
    Generates a dictionary for resilient pagination in a hypermedia dataset.
    - 'index': Integer for start point of data retrieval, defaults to None.
    - 'page_size': Integer for number of items to retrieve, defaults to 10.
    Iterates over the dataset within the 'page_size', compiles a list of data
    items and calculates 'next_index' for subsequent retrievals.
    """
    # The following line has been edited to resolve W293
    assert isinstance(index, int) or index is None
    assert isinstance(page_size, int)
    assert index is None or 0 <= index < len(self.__indexed_dataset)

    data = []  # Data items list
    # Start index; resolved E501 by splitting the line
    current_index = index if index is not None else 0  
    next_index = current_index  # Next index for pagination

    # Iterate and retrieve data; resolved E501 by splitting the condition
    while len(data) < page_size and \
          current_index < len(self.__indexed_dataset):
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
