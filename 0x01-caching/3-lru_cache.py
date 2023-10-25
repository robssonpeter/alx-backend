#!/usr/bin/env python3
""" The caching module that uses LRU Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ The class that uses LRU Caching """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ ### The method for putting an entry into cache
            Its quite interesting here
        """
        if key is not None and item is not None:
            keys = list(self.cache_data.keys())
            if len(keys) >= self.MAX_ITEMS:
                if key in keys:
                    value = self.cache_data[key]
                    del self.cache_data[key]
                    self.cache_data[key] = item
                else:
                    """ Remove the first item """
                    keys = list(self.cache_data.keys())
                    first_key = keys[0]
                    print(f"DISCARD: {first_key}")
                    del self.cache_data[first_key]
                    self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ The function to retrieve a certain key from cache"""
        keys = self.cache_data.keys()
        if key is None:
            return None
        if key not in keys:
            return None
        """ Delete the key and move it to the end """
        value = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = value
        return self.cache_data[key]
