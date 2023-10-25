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
            deleted = False
            if key in self.cache_data.keys():
                del self.cache_data[key]
                deleted = True
            self.cache_data[key] = item
            keys = list(self.cache_data.keys())
            if len(keys) >= self.MAX_ITEMS:
                """ Remove the last element """
                last_key = keys[len(keys) - 1]
                """Remove only if the key is not there """
                if not deleted:
                    print(f'DISCARD: {last_key}')
                    del self.cache_data[last_key]
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
