#!/usr/bin/env python3

def zad32_3(n,napis):
    tmp = []
    ret = []
    i = 0
    while i <= n:
        if napis[i] not in ('(', ')'):
            ret.append(napis[i])
            i += 1
        else:
            i += 1 
            if i >= n:
                break
            while napis[i] != ')' and i <= n:
                ret.append(napis[i])
                tmp.append(napis[i])
                i += 1
            ret += tmp
    return ret

napis = '(ab)'
print(zad32_3(len(napis), napis))

