#!/usr/bin/env python3
import csv
import math
from typing import List
from typing import Tuple
""" The module to define a function index_range """


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ The function index range """
    last_element = page * page_size
    first_element = last_element - page_size
    return (first_element, last_element)

if __name__ == "__main__":
    print(index_range(8, 9))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """ This method is going to return the page a list of thing """
            assert isinstance(page, int) and page > 0, AssertionError('AssertionError raised with negative values')
            assert isinstance(page_size, int) and page_size > 0, AssertionError('AssertionError raised with negative values')
            if page == 0:
                 raise AssertionError('AssertionError raised with 0')
            elif isinstance(page_size, int) is False:
                raise AssertionError('AssertionError raised when page and/or page_size are not ints')

            indexes = index_range(page, page_size)

            data = self.dataset()
            if (page > len(data)/page_size):
                 return []

            return data[indexes[0]: indexes[1]]
