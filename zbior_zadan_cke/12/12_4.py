#!/usr/bin/env python3

### Pierwsza wersja
def dekoduj(n, tekst, k):
    ret = []
    for i in range(0, n):
        tmp = ord(tekst[i])
        x = 0
        while ((90 + k  - 26*x) + 65 - tmp) not in range(65, 91):
            x += 1
        k += i
        ret.append(chr((90 + k  - 26*x) + 65 - tmp))
    return ''.join(ret)

### Druga wersja
def dekoduj2(n, tekst,k):
    ret= []
    i=0
    while i <n:
        ret.append(chr((90-ord(tekst[i])+k) % 26 + 65))
        i += 1
        k += i
    return ''.join(ret)


if __name__ == "__main__":
    k = 14
    tekst = "DAN"
    print(dekoduj(len(tekst), tekst, k))
    print(dekoduj2(len(tekst), tekst, k))
