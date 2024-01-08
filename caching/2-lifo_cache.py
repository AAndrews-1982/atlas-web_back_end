#!/usr/bin/env python3
""" 2. LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching
    and is a LIFO caching system.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key.
        If the cache exceeds its limit, remove the last item added.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.last_key = key

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
