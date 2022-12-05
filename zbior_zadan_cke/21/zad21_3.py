#!/usr/bin/env python3

def oblicz(x,n,k):
    w = 1
    i = n-1
    while i >= 0:
        if k[i] == '1':
            w *= x
        x *= x
        i -= 1
    return w

def oblicz2(x,n,k):
    p = x
    for i in range(n-2, -1, -1):
        p *= p

        if k[i] == '1':
            p *= x

    return p

if __name__ == "__main__":
    print(oblicz(2,2,'11'))
    print(oblicz2(2,2,'11'))
