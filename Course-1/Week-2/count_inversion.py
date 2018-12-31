# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' compute the number of inversions '

__author__ = 'Qiyun Lu'

""" python tester.py ./count_inversion.py ../../testCases/course1/assignment2Inversions """


def sort_and_count(arr):
    
    if len(arr) == 1:
        return (0, arr)

    half_length = int(len(arr) / 2)
    left_part = sort_and_count(arr[:half_length])
    right_part = sort_and_count(arr[half_length:])
    left_amount = left_part[0]
    left_sorted_arr = left_part[1]
    right_amount = right_part[0]
    right_sorted_arr = right_part[1]

    split_part = merge_and_count_split(left_sorted_arr, right_sorted_arr)
    split_amount = split_part[0]
    total_sorted_arr = split_part[1]

    return (split_amount + left_amount + right_amount, total_sorted_arr)

def merge_and_count_split(left_sorted_arr, right_sorted_arr):
    
    arr_x = left_sorted_arr
    arr_y = right_sorted_arr
    amount = 0
    sorted_arr = []
    pointer_x = 0
    pointer_y = 0
    
    while True:
        if arr_x[pointer_x] > arr_y[pointer_y]:
            sorted_arr.append(arr_y[pointer_y])
            pointer_y += 1
            amount += (len(arr_x) - pointer_x)
        else:
            sorted_arr.append(arr_x[pointer_x])
            pointer_x += 1
        if pointer_x == len(arr_x):
            sorted_arr += arr_y[pointer_y:]
            break
        elif pointer_y == len(arr_y):
            sorted_arr += arr_x[pointer_x:]
            break
    
    return (amount, sorted_arr)

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
        item = lines[i].strip()
        i += 1
        if item != '':
            arr.append(int(item))

    return sort_and_count(arr)[0]

