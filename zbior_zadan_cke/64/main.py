#!/usr/bin/env python3
# 17.02.2022 by neloduka_sobe
# taki spagetti code (szczególnie 4 podpunkt), że aż wstyd mi za to, że to działa
# TODO refaktoryzacja tego potwora

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
            print("Zadanie 64.2")
            print(f"Ostatnia linia pierwszego obrazka rekurencyjnego: {i}")

print(f"Ilość: {ilosc}")

### 64.3

linie = []
with open("dane/dane_obrazki.txt", "r") as f:
    for line in f:
        linie.append(line.strip())

maks = 0
poprawne = 0
naprawialne = 0
licznik = 0
bledy_po = 0
bledy_pi = 0
pion = [0 for z in range(20)]

# do pp. 4
pp4 = dict()
pp4i1 = -1
pp4i2 = -1
obrazek = 0

for i in range(len(linie)):
    if licznik < 20 and len(linie[i]) == 21:
        obraz = linie[i][:-1]
        parzystosc = int(linie[i][-1])
        for ind in range(len(obraz)):
            pion[ind] = pion[ind] + int(obraz[ind])

        if parzystosc != sum([int(a) for a in obraz]) % 2:
            pp4i1 = licznik+1 # do pp. 4
            bledy_po += 1

        licznik += 1

    elif licznik == 20:
        obrazek += 1 # do pp. 4
        licznik = 0
        linia = linie[i]
        for ind in range(len(pion)):
            if pion[ind] % 2 != int(linia[ind]):
                pp4i2 = ind+1 # do pp. 4
                bledy_pi += 1
        if bledy_po + bledy_pi > maks:
            maks = bledy_po + bledy_pi

        if bledy_po == bledy_pi == 0:
            poprawne += 1

        elif bledy_po <= 1 and bledy_pi <= 1:
            naprawialne += 1

            # do pp. 4
            if bledy_po == 1 == bledy_pi:
                pp4[obrazek] = (pp4i1, pp4i2, (int(linie[pp4i1][pp4i2])+1) % 2)
            elif bledy_po == 0 and bledy_pi == 1:
                pp4[obrazek] = (21, pp4i2,  (int(linia[pp4i2])+1) % 2)
            elif bledy_po == 1 and bledy_pi == 0:
                pp4[obrazek] = (pp4i1, 21,  int(linie[pp4i1][-1])+1 % 2)

        
        bledy_pi, bledy_po = 0,0
        pion = [0 for z in range(20)]

        # do pp. 4
        pp4i1 = -1
        pp4i2 = -1

print("Zadanie 64.3")
print(f"Naprawialne: {naprawialne}")
print(f"Poprawne: {poprawne}")
print(f"Nienaprawialne: {200 - naprawialne - poprawne}")
print(f"Max błędów: {maks}")

### 64.4

print("Zadanie 64.4")
for i in pp4.keys():
    print(f"Nr obrazka: {i}; Dane: {pp4[i]}")
