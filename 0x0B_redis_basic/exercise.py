#!/usr/bin/env python3
"""
This module defines a Cache class for storing data in Redis with random keys.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    A Cache class to store data in Redis using randomly generated keys.
    """

    def __init__(self) -> None:
        """
        Initialize the Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()  # Clean start

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis under a random key.

        :param data: Data to store (str, bytes, int, float).
        :return: The random key for the data.
        """
        # Generate a unique key
        key = str(uuid.uuid4())
        # Store data with the generated key
        self._redis.set(name=key, value=data)
        return key


# Example of using the Cache class
if __name__ == "__main__":
    cache = Cache()
    key = cache.store("Hello, Redis!")
    print(f"Data stored under key: {key}")
