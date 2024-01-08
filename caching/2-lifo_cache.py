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
        self.key_order = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key.
        If the cache exceeds its limit, remove the last
        item added.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)

            while len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(-2)
                # Discarding the last item before the new one
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
