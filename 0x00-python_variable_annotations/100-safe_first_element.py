#!/usr/bin/env python3
"""module that safely retrieve the first element of the input list"""
from typing import Any, Union


def safe_first_element(lst) -> Union[Any, None]:
    """return The first element of the list"""
    if lst:
        return lst[0]
    else:
        return None
