#!/usr/bin/env python3

### Wczytywanie danych
dokad = ''
with open('dane/dokad.txt', 'r') as f:
    for line in f:
        dokad = line.strip()

szyfr = []
with open('dane/szyfr.txt', 'r') as f:
    for line in f:
        szyfr.append(line.strip())

litery = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

### Funkcje
def zaszyfruj(tekst, klucz):
    ilosc_innych_znakow = 0
    wynik = ''

    for i in range(len(tekst)):
        y = (i-ilosc_innych_znakow) % len(klucz)

        if tekst[i] not in litery:
            wynik += tekst[i]
            ilosc_innych_znakow += 1
            continue 

        wynik += litery[(litery.index(tekst[i]) + litery.index(klucz[y])) % 26]
    return wynik, round((len(tekst)-ilosc_innych_znakow)/12)

def odszyfruj(tekst, klucz):
    ilosc_innych_znakow = 0
    wynik = ''

    for i in range(len(tekst)):
        y = (i-ilosc_innych_znakow) % len(klucz)

        if tekst[i] not in litery:
            wynik += tekst[i]
            ilosc_innych_znakow += 1
            continue 

        wynik += litery[(litery.index(tekst[i]) - litery.index(klucz[y])) % 26]
    return wynik

### Zadanie 77.1
print(f"Zadanie 77.1\n{zaszyfruj(dokad, 'LUBIMYCZYTAC')}")

### Zadanie 77.2
print(f"Zadanie 77.2\n{odszyfruj(szyfr[0], szyfr[1])}")

### Zadanie 77.3
print("Zadanie 77.3 a)")
wystepowanie = dict()
n = 0
for i in list(litery):
    print(f"{i}: {szyfr[0].count(i)}")
    wystepowanie[i] = szyfr[0].count(i)
    n += szyfr[0].count(i)

k = (sum([wystepowanie[i] * (wystepowanie[i]-1) for i in wystepowanie.keys()]) / (n * (n-1)))
d = (0.0285) / (k - 0.0385)

print(f"Zadanie 77.3 b) Szacowana: {round(d, 2)} Realna: {len(szyfr[1])}")
