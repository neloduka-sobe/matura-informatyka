#!/usr/bin/env python3

### Funkcje

# Funkcja szyfrująca
def przestawieniowy(tekst, klucz):

    tekst = list(tekst)
    klucz = [int(i)-1 for i in klucz]

    for i in range(len(tekst)):
        tekst[i], tekst[klucz[i % len(klucz)]] = tekst[klucz[i % len(klucz)]], tekst[i]
    return ''.join(tekst)


# Funkcja deszyfrująca
def deszyfr(tekst, klucz):

    tekst = list(tekst)
    klucz = [int(i)-1 for i in klucz]

    for i in range(len(tekst)-1, -1,-1):
        tekst[i], tekst[klucz[i % len(klucz)]] = tekst[klucz[i % len(klucz)]], tekst[i]
    return ''.join(tekst)

# Testy funkcji na przykładzie
#print(przestawieniowy('INFORMATYKA', [3,2,5,4,1]))
#print(deszyfr("KAAYTRNFOIM",[3,2,5,4,1] ))

### Zadanie 76.1
szyfr1 = []

with open('dane/szyfr1.txt', 'r') as f:
    for line in f:
        szyfr1.append(line.strip())
szyfr1[-1] = [int(i) for i in szyfr1[-1].split(' ')]

with open('wyniki_szyfr1.txt', 'w') as f:
    for i in range(6):
        f.write((przestawieniowy(szyfr1[i], szyfr1[-1])))
        f.write('\n')


### Zadanie 76.2
szyfr2 = []
with open('dane/szyfr2.txt', 'r') as f:
    for line in f:
        szyfr2.append(line.strip())
szyfr2[-1] = [int(i) for i in szyfr2[-1].split(' ')]

with open('wyniki_szyfr2.txt', 'w') as f:
    f.write(f'{przestawieniowy(szyfr2[0], szyfr2[1])}\n')


### Zadanie 76.3
szyfr3 = []
with open('dane/szyfr3.txt', 'r') as f:
    for line in f:
        szyfr3.append(line.strip())

with open('wyniki_szyfr3.txt', 'w') as f:
    f.write(f"{deszyfr(szyfr3[0], [6,2,4,1,5,3])}\n")
