# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' quicksort '

__author__ = 'Qiyun Lu'


class Quicksort(object):

    '''
    do quicksort

    >>> qsort = Quicksort()
    >>> qsort.sort([])
    []
    >>> qsort.sort([9, 7, 5, 3, 1])
    [1, 3, 5, 7, 9]
    >>> arr01 = [2]
    >>> arr01 = qsort.sort(arr01)
    >>> print(arr01)
    [2]
    >>> arr02 = [2, 6, 0, 8, 4]
    >>> arr02 = qsort.sort(arr02)
    >>> print(arr02)
    [0, 2, 4, 6, 8]
    '''

    def sort(self, arr, left_border = None, right_border = None):
        
        if left_border == None:
            left_border = 0
        if right_border == None:
            right_border = len(arr) - 1
        if left_border >= right_border:
            return arr
        
        head = left_border
        tail = right_border
        pivot_ptr = tail
        pivot = arr[pivot_ptr]

        while head != tail:
            while head < pivot_ptr:
                if arr[head] > pivot:
                    arr[pivot_ptr] = arr[head]
                    arr[head] = pivot
                    pivot_ptr = head
                    break
                head += 1
            while tail > pivot_ptr:
                if arr[tail] < pivot:
                    arr[pivot_ptr] = arr[tail]
                    arr[tail] = pivot
                    pivot_ptr = tail
                    break
                tail -= 1
        
        self.sort(arr, left_border, pivot_ptr - 1)
        self.sort(arr, pivot_ptr + 1, right_border)

        return arr


if __name__ == '__main__':

    import doctest
    doctest.testmod()
