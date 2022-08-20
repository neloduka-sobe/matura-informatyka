#!/usr/bin/env python3

dane = []

### Wczytywanie danych
with open('dane/okregi.txt', 'r') as f:
    for line in f:
        dane.append([float(i) for i in line.strip().split()])

### Zadanie 79.1

def cwiartka(x,y,r):
    if x-r > 0 and y - r > 0:
        return 1
    elif x+r < 0 and y - r > 0:
        return 2
    elif y+r < 0 and x + r < 0:
        return 3
    elif x-r > 0 and y + r < 0:
        return 4
    else:
        return 5

ilosc = [0,0,0,0,0]
for i in dane:
    ilosc[cwiartka(i[0], i[1], i[2])-1] += 1

print(f"Zadanie 79.1: {ilosc}")

### Zadanie 79.2

def odbicia(x,y,r):
    return [[-x, y, r], [x, -y, r]]

ilosc2 = 0
for i in dane:
    for y in odbicia(i[0], i[1], i[2]):
        if y in dane and dane.index(y) > dane.index(i):
            ilosc2 += 1

print(f"Zadanie 79.2: {ilosc2}")

### Zadanie 79.3

def o_90_st(x,y, r):
    return [-y, x, r]

ilosc3 = 0
for i in dane:
    if o_90_st(i[0],i[1], i[2]) in dane:
        ilosc3 += 1
print(f"Zadanie 79.3: {ilosc3}")

### Zadanie 79.4

dlugosci = []
last = [9*(10**100) for i in range(3)]
dl = 0

def pkt_wspolny(okr1, okr2):
    [x1,y1,r1],[x2,y2,r2] = okr1, okr2
    tmp = ((x2-x1)**2 + (y2-y1)**2)**0.5 
    return r1+r2 >= tmp and abs(r1-r2) <= tmp 

for i in range(1000):
    if pkt_wspolny(last, dane[i]):
        dl += 1
    else:
        dlugosci.append(dl)
        dl = 1

    last = dane[i]

print(f"Zadanie 79.4: {max(dlugosci)}")
