#!/usr/bin/env python3
""" The caching module that uses MRU Caching """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ The class that uses MRU Caching """
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
                    del self.cache_data[key]
                    self.cache_data[key] = item
                else:
                    """ Remove the first item """
                    keys = list(self.cache_data.keys())
                    last_key = keys[len(keys) - 1]
                    print(f"DISCARD: {last_key}")
                    del self.cache_data[last_key]
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
