#!/usr/bin/env python3

def rozklad(x):
    pierw = int(x**0.5)

    if x == 1:
        return []

    ret = []
    i = 2

    while x > 1 and i <= pierw:
        while x % i == 0:
            ret.append(i)
            x //= i
        i+= 1
    if x > 1:
        ret.append(x)
    return ret

if __name__ == "__main__":
    print(rozklad(24))
