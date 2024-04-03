#!/usr/bin/env python3

from base_caching import BaseCaching


class BaseCache:
    """
    This caching system doesn’t have limit
    def put(self, key, item):
    assign to the dictionary self.cache_data the item value for the key key.
    If key or item is None, this method should not do anything.
    """
    cache_data = {}

    def put(self, key, item):
        """ Put an item in cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
