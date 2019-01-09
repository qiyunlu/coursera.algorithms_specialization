# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' select the i th smallest element in the array '

__author__ = 'Qiyun Lu'


import random
import doctest

def randomized_selection(array, i):
    
    '''
    >>> randomized_selection([], 2)

    >>> randomized_selection([1000], 6)
    1000
    >>> randomized_selection([1,3,5,7,9], 4)
    7
    >>> randomized_selection([10,8,6,4,2], 2)
    4
    >>> randomized_selection(list(range(86420)), 13579)
    13578
    '''

    array = list(array)
    arr_len = len(array)
    # empty array
    if arr_len == 0:
        return None
    # only one element in the array
    if arr_len == 1:
        return array[0]
    
    # choose a pivot randomly
    pivot_ptr = random.randrange(arr_len)
    pivot = array[pivot_ptr]

    # partition the array
    array[pivot_ptr] = array[0]
    array[0] = pivot
    # the pointer of the first element that bigger than pivot
    split_ptr = 1
    # the pointer of the first element of unpartitioned part
    unpartitioned_ptr = 1
    while unpartitioned_ptr < arr_len:
        if array[unpartitioned_ptr] < pivot and unpartitioned_ptr != split_ptr:
            # swap (if partitioned part has at least one element that is bigger than pivot)
            _swap = array[unpartitioned_ptr]
            array[unpartitioned_ptr] = array[split_ptr]
            array[split_ptr] = _swap
            split_ptr += 1
        elif array[unpartitioned_ptr] < pivot:
            # no swap (no partitioned element bigger than pivot) but split_ptr increase 1
            split_ptr += 1
        # unpartitioned_ptr move forward
        unpartitioned_ptr += 1
    # swap pivot to the right place
    pivot_ptr = split_ptr - 1
    array[0] = array[pivot_ptr]
    array[pivot_ptr] = pivot

    # recursion
    if pivot_ptr + 1 == i:
        # really lucky
        return pivot
    elif pivot_ptr + 1 > i:
        return randomized_selection(array[:pivot_ptr], i)
    else:
        return randomized_selection(array[pivot_ptr+1:], i-pivot_ptr-1)


if __name__ == '__main__':
    pass
    doctest.testmod()
    