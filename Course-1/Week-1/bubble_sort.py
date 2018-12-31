# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' bubble sort '

__author__ = 'Qiyun Lu'


class Bubble_Sort(object):

    '''
    do bubble sort

    >>> bsort = Bubble_Sort()
    >>> bsort.sort([])
    []
    >>> bsort.sort([9, 7, 5, 3, 1])
    [1, 3, 5, 7, 9]
    >>> arr01 = [2]
    >>> arr01 = bsort.sort(arr01)
    >>> print(arr01)
    [2]
    >>> arr02 = [2, 6, 0, 8, 4]
    >>> arr02 = bsort.sort(arr02)
    >>> print(arr02)
    [0, 2, 4, 6, 8]
    '''

    def sort(self, arr):
        
        turn = 0
        
        while turn < len(arr) - 1:
            border = len(arr) - turn - 1
            no_swap = True
            i = 0
            while i < border:
                if arr[i] > arr[i+1]:
                    _v = arr[i+1]
                    arr[i+1] = arr[i]
                    arr[i] = _v
                    no_swap = False
                i += 1
            if no_swap:
                break

        return arr


if __name__ == '__main__':

    import doctest
    doctest.testmod()
