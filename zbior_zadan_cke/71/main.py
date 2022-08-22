#!/usr/bin/env python3

### Wczytywanie danych
dane = []

with open('dane/funkcja.txt', 'r') as f:
    for line in f:
        dane.append([float(i) for i in line.strip().split()])

def war(tab,x):
    for i in range(0,5):
        if x >= i and x <= i+1:
            return tab[i][0] + tab[i][1]*(x) + tab[i][2]*(x**2) + tab[i][3]*(x**3) 

### Zadanie 71.1
print("Zadanie 71.1")
print(round(war(dane, 1.5),5))


### Zadanie 71.2
maks = 0
maks_x = 0
for i in range(0,5001):
    i /= 1000
    w = war(dane, i)
    if w > maks:
        maks = w
        maks_x = i

print(f"\nZadanie 71.2: f(x) = {round(maks,5)}, x = {maks_x}")

### Zadanie 71.3
msc_zer = []
last = -1
for i in range(0,5000001):
    i /= 1000000
    w = war(dane, i)
    if (last <= 0 and w >= 0) or (w <= 0 and last >= 0):
        msc_zer.append(round(i,5))
    last = w

print("\nZadanie 71.3")
print(msc_zer)
