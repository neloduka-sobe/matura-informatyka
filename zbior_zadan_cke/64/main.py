#!/usr/bin/env python3


### 64.1 
ilosc = 0
maks = 0
with open("dane/dane_obrazki.txt" ,'r') as f:
    ilosc1 = 0
    for line in f:
        line = (line.strip())[:-1]
        if len(line) == 19:
            if ilosc1 > 200:
                ilosc += 1
            if ilosc1 > maks:
                maks = ilosc1
            ilosc1 = 0
            continue

        if len(line) == 20:
           ilosc1 += line.count('1') 

print("Zadanie 64.1")
print(f"Ilość: {ilosc}")
print(f"Max: {maks}")

### 64.2
linie = []
with open("dane/dane_obrazki.txt", "r") as f:
    for line in f:
        linie.append(line.strip())

tile = []
tile2 = []
tile3 = []
tile4 = []
ilosc = 0
licznik = 0
for i in range(len(linie)):

    if len(linie[i]) == 20 or len(linie[i]) == 0:
        tile = []
        tile2 = []
        tile3 = []
        tile4 = []
        licznik = 0
        continue

    linie[i] = linie[i][:20]

    if licznik < 10:
        tile.append(linie[i][:10])
        tile2.append(linie[i][10:])
        licznik += 1
    elif licznik >= 10:
        tile3.append(linie[i][:10])
        tile4.append(linie[i][10:])
        licznik += 1

    if tile == tile2 == tile3 == tile4:
        ilosc += 1
        if ilosc == 1:
            print(f"Ostatnia linia pierwszego obrazka rekurencyjnego: {i}")

print("Zadanie 64.2")
print(f"Ilość: {ilosc}")
