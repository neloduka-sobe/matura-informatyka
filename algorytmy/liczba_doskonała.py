#!/usr/bin/env python3

def liczba_doskonala_1(x):
    s = 1
    for i in range(2,x):
        if x % i == 0:
            s += i
    return s == x

def liczba_doskonala_2(x):
    s = 1
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            s += i
            if i != x//i:
                s += x//i
    return s == x

if __name__ == "__main__":
    print(liczba_doskonala_1(6))
    print(liczba_doskonala_1(28))
    print(liczba_doskonala_1(100))
    print(liczba_doskonala_2(6))
    print(liczba_doskonala_2(28))
    print(liczba_doskonala_2(100))
