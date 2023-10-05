#!/usr/bin/env python3
"""module that safely retrieve the first element of the input list"""
from typing import Any, Union


def safe_first_element(lst) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
