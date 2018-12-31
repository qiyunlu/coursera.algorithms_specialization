# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' karatsuba multiplication '

__author__ = 'Qiyun Lu'

""" python tester.py ./karatsuba_multiplication.py ../../testCases/course1/assignment1Multiplication """

def karatsuba(x, y):
    
    x = str(x)
    y = str(y)
    
    if x == '0' or y == '0':
        return 0
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
            
    total_len = max(len(x), len(y))
    high_len = int(total_len / 2)
    low_len = total_len - high_len
    
    b = x[-low_len:]
    a = x[:-low_len]
    d = y[-low_len:]
    c = y[:-low_len]
    if a == '':
        a = '0'
    if c == '':
        c = '0'
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(int(a)+int(b), int(c)+int(d))
    sub = abcd - ac - bd
    
    return pow(10, low_len*2)*ac + pow(10, low_len)*sub + bd


def alg(file_path):
    
    try:
        f = open(file_path, 'r')
        lines = f.readlines()
        x = lines[0].strip()
        y = lines[1].strip()
    finally:
        if f:
            f.close()

    return karatsuba(x, y)


if __name__ == '__main__':
    pass
    result = karatsuba('12345678998765432112345678987654321', '1212121212121234343434343434343434444444444')
    assert result == 14964459392443222363386654166355210140914770544956011896745221548821561042524, 'Wrong!'
    print("12345678998765432112345678987654321 * 1212121212121234343434343434343434444444444 = {}".format(result))
    