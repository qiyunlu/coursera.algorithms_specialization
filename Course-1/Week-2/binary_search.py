# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' binary search '

__author__ = 'Qiyun Lu'


def binary_search(arr, target, left_ptr = None, right_ptr = None):

    '''
    >>> binary_search([], 5)
    
    >>> binary_search([5], 5)
    0
    >>> binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    3
    >>> binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
    8
    >>> binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -1)
    
    '''

    if left_ptr == None:
        left_ptr = 0
    if right_ptr == None:
        right_ptr = len(arr) - 1

    if arr == []:
        return None
    if left_ptr > right_ptr:
        return None

    middle_ptr = int((left_ptr + right_ptr) / 2)
    if arr[middle_ptr] == target:
        return middle_ptr
    elif arr[middle_ptr] > target:
        return binary_search(arr, target, left_ptr=left_ptr, right_ptr=middle_ptr-1)
    else:
        return binary_search(arr, target, left_ptr=middle_ptr+1, right_ptr=right_ptr)


if __name__ == '__main__':

    import doctest
    doctest.testmod()
