#!/usr/bin/env python3
# 10.03.2022 by neloduka_sobe

dane = []
with open("dane/napisy.txt", "r") as f:
    for line in f:
        line = line.strip().split(" ")
        dane.append(line)


### 72.1
print("Zadanie 72.1")
ilosc = 0

for i in dane:
    if max(len(i[0]), len(i[1])) >= 3 * min(len(i[0]), len(i[1])):
        if ilosc == 0:
            print("Pierwszy:", *i)
        ilosc += 1

print(f"Ilość: {ilosc}")


### 72.2
print("Zadanie 72.2")
for i in dane:
    if len(i[1]) != len(i[0]):
        dl = max(i[0], i[1], key = lambda x: len(x))
        kr = min(i[0], i[1], key = lambda x: len(x))
        if kr in dl and dl.index(kr) == 0:
            print(f"Linia: {i}")
            print(f"Ciąg: {dl[len(kr):]}")

### 72.3
zak = dict()

for i in dane:
    ilosc = 0
    for y in range(-1, -min(len(i[0]),  len(i[1]))-1, -1):
        if i[1][y] == i[0][y]:
            ilosc += 1
        else:
            if ilosc not in zak.keys():
                zak[ilosc] = [i]
            else:
                zak[ilosc] = zak[ilosc] + [i]
            break

print("Zadanie 72.3")
maks = max(zak.keys())
print(f"Długość: {maks}")
print("Pary:")
for i in zak[maks]:
    print(i)
