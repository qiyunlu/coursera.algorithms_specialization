# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' selection sort '

__author__ = 'Qiyun Lu'


class Selection_Sort(object):

    '''
    do selection sort

    >>> ssort = Selection_Sort()
    >>> ssort.sort([])
    []
    >>> ssort.sort([9, 7, 5, 3, 1])
    [1, 3, 5, 7, 9]
    >>> arr01 = [2]
    >>> arr01 = ssort.sort(arr01)
    >>> print(arr01)
    [2]
    >>> arr02 = [2, 6, 0, 8, 4]
    >>> arr02 = ssort.sort(arr02)
    >>> print(arr02)
    [0, 2, 4, 6, 8]
    '''

    def sort(self, arr):
        
        base_ptr = 0

        while base_ptr < len(arr) - 1:
            current_min = base_ptr
            current_ptr = base_ptr + 1
            while current_ptr < len(arr):
                if arr[current_ptr] < arr[current_min]:
                    current_min = current_ptr
                current_ptr += 1
            _min = arr[current_min]
            arr[current_min] = arr[base_ptr]
            arr[base_ptr] = _min
            base_ptr += 1

        return arr


if __name__ == '__main__':

    import doctest
    doctest.testmod()
