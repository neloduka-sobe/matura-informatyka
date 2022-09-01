#!/usr/bin/env python3

def zad32_2(n, napis):
    if n % 2 == 0:
        if ''.join(napis[:((n//2))]) == ''.join(napis[((n//2)):]):
            return ''.join(napis[:((n//2))])
    else:
        return 0


print(zad32_2(8, list('abcaabca')))
