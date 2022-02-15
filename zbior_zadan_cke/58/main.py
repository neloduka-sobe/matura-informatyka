#!/usr/bin/env python3
# 15.02.2022 by neloduka_sobe

import math

# Wczytywanie danych
temperatury1 = []
systemy1 = []

with open("dane/dane_systemy1.txt", "r") as f:
    for line in f:
        czas, temperatura = line.strip().split(" ")
        czas, temperatura = int(czas, 2), int(temperatura, 2)
        temperatury1.append(temperatura) 
        systemy1.append([czas, temperatura])

temperatury2 = []
systemy2 = []
with open("dane/dane_systemy2.txt", "r") as f:
    for line in f:
        czas, temperatura = line.strip().split(" ")
        czas, temperatura = int(czas, 4), int(temperatura, 4)
        temperatury2.append(temperatura) 
        systemy2.append([czas, temperatura])

temperatury3 = []
systemy3 = []
with open("dane/dane_systemy3.txt", "r") as f:
    for line in f:
        czas, temperatura = line.strip().split(" ")
        czas, temperatura = int(czas, 8), int(temperatura, 8)
        temperatury3.append(temperatura) 
        systemy3.append([czas, temperatura])

### 58.1
print("Zadanie 58.1:")
print(f"Pierwsza stacja: {bin(min(temperatury1))}")
print(f"Druga stacja: {bin(min(temperatury2))}")
print(f"Trzeci stacja: {bin(min(temperatury3))}")


### 58.2
licznik = 0
for i in range(0, 1095):
    if systemy3[i][0] % 24 != 12 and systemy2[i][0] % 24 != 12 and systemy1[i][0] % 24 != 12:
        licznik += 1
print("Zadanie 58.2:")
print(f"Liczba pomiarów: {licznik}")


### 58.3
rekord1 = -999999999999
rekord2 = -999999999999
rekord3 = -999999999999
dni_rekordowe = 0

for i in range(0, 1095):
    rekord = False

    if temperatury1[i] > rekord1:
        rekord = True
        rekord1 = temperatury1[i]

    if temperatury2[i] > rekord2:
        rekord = True
        rekord2 = temperatury2[i]

    if temperatury3[i] > rekord3:
        rekord = True
        rekord3 = temperatury3[i]
    
    if rekord:
        dni_rekordowe += 1

print("Zadanie 58.3:")
print(f"Dni rekordowe: {dni_rekordowe}")


### 58.4
def skok_temp(i,j,ti, tj):
    rij = (ti-tj)**2
    return math.ceil(rij/abs(i-j))

maks = 0
for i in range(1, 1096):
    for j in range(1, 1096):
        if i == j:
            continue

        s = skok_temp(i,j,temperatury1[i-1], temperatury1[j-1])
        if  s > maks:
            maks = s
print("Zadanie 58.4:")
print(f"Największy skok: {maks}")
