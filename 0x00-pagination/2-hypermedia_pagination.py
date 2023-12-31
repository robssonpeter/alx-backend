#!/usr/bin/env python3
import csv
import math
from typing import List
from typing import Tuple
from typing import Dict
""" The module to define a function index_range """


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ The function index range """
    last_element = page * page_size
    first_element = last_element - page_size
    return (first_element, last_element)


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
        ng_msg = 'AssertionError raised with negative values'
        page_is_int = isinstance(page, int)
        size_is_int = isinstance(page_size, int)
        assert page_is_int and page > 0, AssertionError(ng_msg)
        assert size_is_int and page_size > 0, AssertionError(ng_msg)
        if page == 0:
            raise AssertionError('AssertionError raised with 0')
        elif isinstance(page_size, int) is False:
            msg = """
            AssertionError raised when page and/or page_size are not ints
            """
            raise AssertionError(msg)

        indexes = index_range(page, page_size)

        data = self.dataset()
        """ The inputs are out of range """
        if (page > math.ceil(len(data) / page_size)):
            return []

        return data[indexes[0]: indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Returns a dictionary of the result with some extra info """
        data = self.get_page(page, page_size)
        pages = math.ceil(len(self.dataset())/page_size)
        next_page = page + 1 if page < pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": pages
        }
