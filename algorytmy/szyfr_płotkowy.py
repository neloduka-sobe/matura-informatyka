#!/usr/bin/env python3
# by neloduka_sobe

### Funkcja
def szyfr(tekst, klucz):
    dl, i, a = 0, 0, []
    while dl < len(tekst):
        a.append([])
        dl += klucz[i]
        i += 1
        i %= len(klucz)
    
    i, ind, y = 0, 0, 0
    while ind  < len(tekst):
        y %= len(klucz)
        a[i] = tekst[ind:(klucz[y]+ind)]
        ind += klucz[y]
        y += 1
        i += 1

    for ind, i in enumerate(a):
        if ind % 4 in (2,3):
            a[ind] = ' ' + i

    '''
    # Sposób 1.
    ret = ''
    for y in range(max(klucz)):
        for i in a:
            if y < len(i):
                ret += i[y]
    return ret
    '''
    # Sposób 2.
    return ''.join([i[y] for y in range(max(klucz)) for i in a if y < len(i) and i[y] != ' '])

### Wywołanie
if __name__ == "__main__":
    print(szyfr("KRYPTOANALIZA", [2,3,2,1]))
    print(de_szyfr("SERFTGNGAIAOA", [2,3,2,1]))
