# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' Algorithm for Closest Pair '

__author__ = 'Qiyun Lu'

import numpy

def merge_sort(arr, coordinate):
    
    if len(arr) == 1:
        return arr
    
    if coordinate in ('x', 'X'):
        axis = 0
    else:
        axis = 1

    left_len = int(len(arr) / 2)
    right_len = len(arr) - left_len

    left_arr = merge_sort(arr[:left_len], coordinate)
    right_arr = merge_sort(arr[left_len:], coordinate)

    merge_arr = []
    left_ptr = 0
    right_ptr = 0
    while True:
        if left_arr[left_ptr][axis] > right_arr[right_ptr][axis]:
            merge_arr.append(right_arr[right_ptr])
            right_ptr += 1
        else:
            merge_arr.append(left_arr[left_ptr])
            left_ptr += 1
        if left_ptr == left_len:
            merge_arr += right_arr[right_ptr:]
            break
        elif right_ptr == right_len:
            merge_arr += left_arr[left_ptr:]
            break
    
    return merge_arr

def closest_pair(point_arr):

    '''
    >>> test_case = ()
    >>> closest_pair(test_case)

    >>> test_case = ((12345,67890),)
    >>> closest_pair(test_case)

    >>> test_case = ((1000000000,-1000000000),(-0.1,0.1))
    >>> closest_pair(test_case)
    ((1000000000, -1000000000), (-0.1, 0.1))
    >>> test_case = ((4,3),(3,2),(2,1),(1,0),(0,-1),(-1,-2),(-2,-3),(-3,-4),(0.5,0.5))
    >>> closest_pair(test_case)
    ((1, 0), (0.5, 0.5))
    >>> test_case = ((9,8),(8,7),(7,6),(6,5),(5,4),(4,4))
    >>> closest_pair(test_case)
    ((5, 4), (4, 4))
    >>> test_case = ((-4,-5),(-5,-6),(-6,-7),(-7,-8),(-8,-9),(-3.9,-3.8))
    >>> closest_pair(test_case)
    ((-4, -5), (-3.9, -3.8))
    >>> test_case = ((1.2,3.4),(5.6,7.8),(9.0,0.1))
    >>> closest_pair(test_case)
    ((5.6, 7.8), (1.2, 3.4))
    '''

    if len(point_arr) in (0, 1):
        return None
    if len(point_arr) == 2:
        return tuple(point_arr)
    
    x_sorted_arr = merge_sort(point_arr, 'x')
    y_sorted_arr = merge_sort(point_arr, 'y')
    return recursive_closest_pair(x_sorted_arr, y_sorted_arr)
    
def recursive_closest_pair(x_sorted_arr, y_sorted_arr):

    if len(x_sorted_arr) == 1:
        if x_sorted_arr == y_sorted_arr:
            return None
        else:
            return (x_sorted_arr[0], y_sorted_arr[0])
    
    left_len = int(len(x_sorted_arr) / 2)
    left_x_arr = x_sorted_arr[:left_len]
    right_x_arr = x_sorted_arr[left_len:]
    left_y_arr = y_sorted_arr[:left_len]
    right_y_arr = y_sorted_arr[left_len:]

    left_candidate = recursive_closest_pair(left_x_arr, left_y_arr)
    right_candidate = recursive_closest_pair(right_x_arr, right_y_arr)
    if left_candidate == None:
        left_distance = float('inf')
    else:
        left_distance = calculate_distance(left_candidate[0], left_candidate[1])
    if right_candidate == None:
        right_distance = float('inf')
    else:
        right_distance = calculate_distance(right_candidate[0], right_candidate[1])
    if left_distance < right_distance:
        recursive_candidate = left_candidate
        recursive_distance = left_distance
    else:
        if right_candidate == None:
            recursive_candidate = None
            recursive_distance = float('inf')
        else:
            recursive_candidate = right_candidate
            recursive_distance = right_distance
    
    split_candidate = split_closest_pair(x_sorted_arr, y_sorted_arr, recursive_distance)
    if split_candidate == None:
        split_distance = float('inf')
    else:
        split_distance = calculate_distance(split_candidate[0], split_candidate[1])
    if split_distance < recursive_distance:
        return split_candidate
    else:
        return recursive_candidate

def calculate_distance(p, q):
    
    return numpy.sqrt(pow(p[0]-q[0], 2) + pow(p[1]-q[1], 2))

def split_closest_pair(x_sorted_arr, y_sorted_arr, recursive_distance):
    
    left_len = int(len(x_sorted_arr) / 2)
    right_len = len(x_sorted_arr) - left_len
    x_middle_point = x_sorted_arr[right_len-1]

    filtered_x_point = []
    for point in x_sorted_arr:
        if abs(point[0]-x_middle_point[0]) <= recursive_distance:
            filtered_x_point.append(point)
    filtered_y_point = []
    for point in y_sorted_arr:
        if point in filtered_x_point:
            filtered_y_point.append(point)

    best = recursive_distance
    best_pair = None
    i = 0
    while i < len(filtered_y_point) - 1:
        j = 1
        while j < min(7, len(filtered_y_point)-i):
            p = filtered_y_point[i]
            q = filtered_y_point[i+j]
            pq_distance = calculate_distance(p, q)
            if pq_distance < best:
                best_pair = (p, q)
                best = pq_distance
            j += 1
        i += 1
    
    return best_pair


if __name__ == '__main__':

    import doctest
    doctest.testmod()
