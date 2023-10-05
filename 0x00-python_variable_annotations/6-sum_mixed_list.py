#!/usr/bin/env python3
"""function sum_mixed_list which takes a list mxd_lst of integers
and floats and returns their sum as a float."""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return The sum of the numbers in 'mxd_lst' as a float"""
    return sum(mxd_lst)
