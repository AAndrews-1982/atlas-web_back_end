#!/usr/bin/env python3
""" 4. MRU Caching
 """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and is a MRU caching system.
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
        If the cache exceeds its limit,
        remove the most recently used item.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the most recently used item
                discarded_key = self.key_order.pop(-1)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end of the list,
        # marking it as most recently used

        self.key_order.remove(key)
        self.key_order.append(key)
        return self.cache_data[key]
