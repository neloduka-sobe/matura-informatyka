#!/usr/bin/env python3

def rekurencyjnie(x, xn):
    if xn == 0:
        return x/2
    return 0.5*(rekurencyjnie(x, xn-1) + x/rekurencyjnie(x, xn-1))

print(rekurencyjnie(169, 10))


def iteracyjnie(x):
    p = x/2
    p2 = 0

    while True:
        p = 0.5 * (p + (x/p))
        if abs(p-p2) < 0.000001:
            break
        p2 = p

    return p

print(iteracyjnie(3))
