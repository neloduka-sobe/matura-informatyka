#!/usr/bin/env python3

def deszyfruj(tekst, k):
    ret = ''
    n = len(tekst)
    for i in range(0,k):
        j = i
        while j < n:
            ret += tekst[j]
            j += k 
    return ret


if __name__ == "__main__":
    print(deszyfruj('SRNZOIYWEFA', 3))
