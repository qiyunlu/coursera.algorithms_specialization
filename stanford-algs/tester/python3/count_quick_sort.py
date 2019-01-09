# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' compute the total number of comparisons used to sort the given input file by QuickSort '

__author__ = 'Qiyun Lu'

""" python tester.py ./count_quick_sort.py ../../testCases/course1/assignment3Quicksort """


import copy
import math

def count_quick_sort(arr, method, left_border = None, right_border = None):

    # default border
    if left_border == None:
        left_border = 0
    if right_border == None:
        right_border = len(arr) - 1
    
    # the length of the subarray
    subarr_len = right_border - left_border + 1
    
    # base case
    if subarr_len <= 1:
        return 0

    # different pivot for different choosing method
    if method == 'first':
        # first element as pivot
        pivot = arr[left_border]
    elif method == 'median':
        # find first, middle, final elements and choose the median one as pivot
        first = arr[left_border]
        middle_ptr = int(subarr_len//2 + subarr_len%2 - 1) + left_border
        middle = arr[middle_ptr]
        final = arr[right_border]
        enumerate_list = [(left_border,first), (middle_ptr,middle), (right_border,final)]
        median = sorted(enumerate_list, key=lambda candidate: candidate[1])[1]
        pivot = median[1]
        pivot_ptr = median[0]
        arr[pivot_ptr] = arr[left_border]
        arr[left_border] = pivot
    else:
        # final element as pivot
        pivot = arr[right_border]
        arr[right_border] = arr[left_border]
        arr[left_border] = pivot

    # partition the subarray
    # the pointer of the first element that bigger than pivot
    split_ptr = left_border + 1
    # the pointer of the first element of unpartitioned part
    unpartitioned_ptr = left_border + 1
    while unpartitioned_ptr <= right_border:
        if arr[unpartitioned_ptr] < pivot and unpartitioned_ptr != split_ptr:
            # swap (if partitioned part has at least one element that is bigger than pivot)
            _swap = arr[unpartitioned_ptr]
            arr[unpartitioned_ptr] = arr[split_ptr]
            arr[split_ptr] = _swap
            split_ptr += 1
        elif arr[unpartitioned_ptr] < pivot:
            # no swap (no partitioned element bigger than pivot) but split_ptr increase 1
            split_ptr += 1
        # unpartitioned_ptr move forward
        unpartitioned_ptr += 1
    # swap pivot to the right place
    pivot_ptr = split_ptr - 1
    arr[left_border] = arr[pivot_ptr]
    arr[pivot_ptr] = pivot

    # partition and recursion
    left_amount = count_quick_sort(arr, method, left_border = left_border, right_border = pivot_ptr-1)
    right_amount = count_quick_sort(arr, method, left_border = pivot_ptr+1, right_border = right_border)

    return (left_amount + right_amount + subarr_len - 1)

def alg(file_path):
    
    try:
        f = open(file_path, 'r')
        lines = f.readlines()
    finally:
        if f:
            f.close()

    arr = []
    i = 0
    while i < len(lines):
        element = lines[i].strip()
        i += 1
        if element != '':
            arr.append(int(element))

    arr_first = copy.deepcopy(arr)
    arr_final = copy.deepcopy(arr)
    arr_median = copy.deepcopy(arr)
    return [count_quick_sort(arr_first, 'first'), count_quick_sort(arr_final, 'final'), count_quick_sort(arr_median, 'median')]


if __name__ == '__main__':
    pass
    result = count_quick_sort([4,3,2,5,1], 'final')
    print(result)