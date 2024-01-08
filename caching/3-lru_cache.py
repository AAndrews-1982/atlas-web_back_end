#!/usr/bin/env python3
""" 3. LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and
    is a LRU caching system.
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
        If the cache exceeds its limit, remove the least
        recently used item.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        # Update the usage order since accessing an
        # item makes it more recently used
        self.key_order.remove(key)
        self.key_order.append(key)
        return self.cache_data[key]
