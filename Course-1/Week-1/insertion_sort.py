# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' insertion sort '

__author__ = 'Qiyun Lu'


class Insertion_Sort(object):

    '''
    do insertion sort

    >>> isort = Insertion_Sort()
    >>> isort.sort([])
    []
    >>> isort.sort([9, 7, 5, 3, 1])
    [1, 3, 5, 7, 9]
    >>> arr01 = [2]
    >>> arr01 = isort.sort(arr01)
    >>> print(arr01)
    [2]
    >>> arr02 = [2, 6, 0, 8, 4]
    >>> arr02 = isort.sort(arr02)
    >>> print(arr02)
    [0, 2, 4, 6, 8]
    '''

    def sort(self, arr):
        
        base_ptr = 1

        while base_ptr < len(arr):
            insert_ptr = base_ptr - 1
            is_inserted = False
            while insert_ptr >= 0:
                if arr[insert_ptr] <= arr[base_ptr]:
                    _value = arr.pop(base_ptr)
                    arr.insert(insert_ptr + 1, _value)
                    is_inserted = True
                    break
                insert_ptr -= 1
            if not is_inserted:
                _value = arr.pop(base_ptr)
                arr.insert(0, _value)
            base_ptr += 1

        return arr


if __name__ == '__main__':

    import doctest
    doctest.testmod()
