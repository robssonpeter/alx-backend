#!/usr/bin/env python3
""" The module for caching for question 0 """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ The class basic cache that extends caching """

    def put(self, key, item):
        """ ### The method for putting an entry into cache
            Its quite interesting here
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ The function to retrieve a certain key from cache"""
        keys = self.cache_data.keys()
        if key is None:
            return None
        if key not in keys:
            return None
        return self.cache_data[key]
