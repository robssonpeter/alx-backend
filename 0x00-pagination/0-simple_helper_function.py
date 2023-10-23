#!/usr/bin/env python3
from typing import Tuple
""" The module to define a function index_range """


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ The function index range """
    last_element = page * page_size
    first_element = last_element - page_size
    return (first_element, last_element)

if __name__ == "__main__":
    print(index_range(8, 9))