# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' Random Contraction Algorithm for Minimum Cut of a Graph '

__author__ = 'Qiyun Lu'

""" python tester.py ./minimum_cut.py ../../testCases/course1/assignment4MinCut """


import random
import math
import copy

def minimum_cut(adj_list):

    # num (n) is the number of vertex
    num = len(adj_list)
    # N is the number of the trial we do, N = n*n*ln(n)
    N = math.ceil(math.pow(num, 2) * math.log(num, math.e))

    min_cut = float('inf')
    # do N times and choose the minimum value
    for i in range(N):
        new_value = random_contraction(copy.deepcopy(adj_list))
        min_cut = min(min_cut, new_value)
    
    return min_cut


def random_contraction(adj_list):

    while len(adj_list) > 2:
        # pick a remaining edge at random
        (u, v) = pick_edge_randomly(adj_list)
        # merge two vertices into one
        merge_vertices(u, v, adj_list)

    crossing_edge_num = 0
    for vertices in adj_list.values():
        # count crossing edges (double)
        crossing_edge_num += len(vertices)

    return int(crossing_edge_num / 2)


def pick_edge_randomly(adj_list):
    
    # choose edge tail
    u = random.choice(list(adj_list.keys()))
    # choose edge head
    v = random.choice(adj_list[u])

    return (u, v)


def merge_vertices(u, v, adj_list):

    # new vertex u
    adj_list[u] += adj_list.pop(v)
    # update the adjacency_list
    for key, value in adj_list.items():
        i = 0
        length = len(value)
        while i < length:
            # redirection
            if adj_list[key][i] == v:
                adj_list[key][i] = u
            # remove self-loops
            if key == adj_list[key][i]:
                adj_list[key].pop(i)
                i -= 1
                length -= 1
            i += 1


def alg(file_path):
    
    try:
        f = open(file_path, 'r')
        lines = f.readlines()
    finally:
        if f:
            f.close()

    adjacency_list = dict()
    for line in lines:
        line = line.strip()
        if line != '':
            elements = line.split(' ')
            adjacency_list[elements[0]] = elements[1:]

    return minimum_cut(adjacency_list)


if __name__ == '__main__':
    pass
    adjacency_list = {'1':['2','3'],'2':['3','4'],'3':['4','1'],'4':['1','2']}
    (u,v) = pick_edge_randomly(adjacency_list)
    print(random_contraction(adjacency_list))