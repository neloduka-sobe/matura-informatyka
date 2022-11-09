#!/usr/bin/env python3

def ln(n,e):
    l1 = 2/3
    l2 = 0
    l3 = float('inf')
    for i in range(0, n+1):
        l3 = l2 + ((1/(2*i+1))*(1/(9**i)))
        if abs(l1*(l3-l2)) < e:
            break
    return l3*l1

print(ln(4, 0.1))
