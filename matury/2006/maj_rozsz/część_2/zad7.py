#!/usr/bin/env python3

dane = []
kursy = []

with open('DANE/lokaty.txt', 'r') as f:
    for line in f:
        dane.append(int(line))

with open('DANE/kursy.txt', 'r') as f:
    for line in f:
        kursy.append(float(line.replace(',', '.')))

### a)
suma_pocz = sum(dane)
suma_kon = 0
maks = 0
for i in dane:
    mnoznik = 0
    if i < 10000.00:
        mnoznik = 1.06
    elif i < 20000.00:
        mnoznik = 1.07
    elif i < 30000.00:
        mnoznik = 1.08
    elif i < 40000.00:
        mnoznik = 1.09
    elif i < 50000.00:
        mnoznik = 1.10
    else:
        mnoznik = 1.11
    if i * mnoznik > maks:
        maks = i*mnoznik
    suma_kon += i * mnoznik

print("Zadanie 7 a)")
print(f"{suma_pocz=}")
print(f"{suma_kon=}")
print(f"{maks=}")
    

### c)
ile = 0
last = kursy[1]
for i in range(2, 365):
    if kursy[i] > last:
        ile += 1
    last = kursy[i]

print("Zadanie 7 c)")
print(f"{ile=}")
