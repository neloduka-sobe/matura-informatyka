#!/usr/bin/env python3

def G(n, T, a, b):
    p = F(1, n, b)
    l = F(1, n, a-1)
    return p - l
