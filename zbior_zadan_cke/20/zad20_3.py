#!/usr/bin/env python3

def bnarc(x, B):
    x_cp = x
    ret = 0
    i = 1
    while (B**(i-1))*(B-1) < x:
        i += 1
    while x >= B:
        ret += (x%B)**i
        x //= B
    ret += x**i
    return ret == x_cp

if __name__ == "__main__":
    print(bnarc(3433, 6))
    print(bnarc(4890, 5))
    print(bnarc(15345, 2))
    print(bnarc(8956, 3))
