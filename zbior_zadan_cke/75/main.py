#!/usr/bin/env python3

### Wczytywanie danych

tekst = []
with open('dane/tekst.txt', 'r') as f:
    for line in f:
        tekst = line.strip().split(' ')



### Funkcje
def afiniczny(tekst, a, b):
    tekst = list(tekst.strip())
    litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    tekst = [litery.index(i) for i in tekst]
    for index, item in enumerate(tekst):
        tekst[index] = litery[(item*a +b)%26]
    return ''.join(tekst)

### Zadanie 75.1
print("Zadanie 75.1")
for i in tekst:
    if i[0] == i[-1] == 'd':
        print(i)

### Zadanie 75.2
print("Zadanie 75.2")
for i in tekst:
    if len(i) >= 10:
        print(afiniczny(i, 5, 2))

### Zadanie 75.3

### Wczytywanie
probka = dict()

with open('dane/probka.txt', 'r') as f:
    for line in f:
        line = line.strip().split()
        probka[line[0]] = line[1]

print("Zadanie 75.3")
for klucz in probka.keys():
    for a in range(0,26):
        for b in range(0,26):
            if afiniczny(klucz, a, b) == probka[klucz]:
                print(f"Klucz szyfrujący dla {klucz} {a=}, {b=}")
            if afiniczny(probka[klucz], a, b) == klucz:
                print(f"Klucz deszyfrujący dla {klucz} {a=}, {b=}")
