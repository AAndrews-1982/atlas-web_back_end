#!/usr/bin/env python3
""" 1. FIFO caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a
    FIFO caching system.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the
        item value for the key key.
        If the cache exceeds its limit, remove the first item added.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.key_order.append(key)
            self.cache_data[key] = item

            while len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
