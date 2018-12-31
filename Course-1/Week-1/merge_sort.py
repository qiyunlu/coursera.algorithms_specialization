# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' merge sort '

__author__ = 'Qiyun Lu'


class Merge_Sort(object):

    '''
    do merge sort

    >>> msort = Merge_Sort()
    >>> msort.sort([])
    []
    >>> msort.sort([9, 7, 5, 3, 1])
    [1, 3, 5, 7, 9]
    >>> arr01 = [2]
    >>> arr01 = msort.sort(arr01)
    >>> print(arr01)
    [2]
    >>> arr02 = [2, 6, 0, 8, 4]
    >>> arr02 = msort.sort(arr02)
    >>> print(arr02)
    [0, 2, 4, 6, 8]
    '''

    def sort(self, arr):
        
        if len(arr) in (0, 1):
            return arr
        
        len_x = int(len(arr) / 2)
        len_y = len(arr) - len_x

        arr_x = self.sort(arr[:len_x])
        arr_y = self.sort(arr[len_x:])

        result = []
        pointer_x = 0
        pointer_y = 0
        while True:
            if arr_x[pointer_x] > arr_y[pointer_y]:
                result.append(arr_y[pointer_y])
                pointer_y += 1
            else:
                result.append(arr_x[pointer_x])
                pointer_x += 1
            if pointer_x == len_x:
                result += arr_y[pointer_y:]
                break
            elif pointer_y == len_y:
                result += arr_x[pointer_x:]
                break
        
        return result


if __name__ == '__main__':

    import doctest
    doctest.testmod()
