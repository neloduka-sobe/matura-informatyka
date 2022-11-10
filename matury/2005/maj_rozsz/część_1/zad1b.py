#!/usr/bin/env python3

def ln(e):
    l = (2/3)
    l1 = float('inf')
    i = 1
    while True:
        l1 = l + 2/3*((1/((2*i)+1))*(1/(9**i)))
        if l1-l < e:
            return l1
        l = l1
        l1 = float('inf')
        i += 1

print(ln(0.0001))
