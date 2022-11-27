#!/usr/bin/env python3

def ss(n):
    """
    Dane:
    n - liczba całkowita >= 1
    Wynik:
    ret - liczba całkowita będąca sumą 1! + 2! + ... + (n-1)! + n!
    """
    ret = 1
    for i in range(n, 1, -1):
        ret *= i
        ret += 1
    return ret

if __name__ == '__main__':
    print(ss(1))
    print(ss(2))
    print(ss(4))
    print(ss(5))

