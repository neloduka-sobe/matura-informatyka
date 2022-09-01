#!/usr/bin/env python3

### Tradycyjnie
def zad27_3(m,n,wzorzec,tekst):

    for i in range(m, n+1):

        ile = 0
        for x,y in zip(tekst[i-m:i+1], wzorzec):
            if x == y:
                ile += 1
        if ile in  (m-1,m):
            return "TAK"

    return "NIE"


wzorzec = 'para'
tekst = 'opera'

print(zad27_3(len(wzorzec), len(tekst), wzorzec, tekst))
