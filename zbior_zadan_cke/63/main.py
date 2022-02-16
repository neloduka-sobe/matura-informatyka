#!/usr/bin/env python3
# 16.02.2022 by neloduka_sobe

# Wczytywanie danych
ciagi = []
with open("dane/ciagi.txt", "r") as f:
    for line in f:
        ciagi.append(line.strip())


### 63.1
print("Zadanie 63.1")
ilosc = 0
for ciag in ciagi:
    if len(ciag) % 2 == 0:
        mid = len(ciag)//2
        if ciag[:mid] == ciag[mid:]:
            print(ciag)
            ilosc += 1

print(f"Ilość wynosi: {ilosc}")


### 63.2
ilosc = 0
for ciag in ciagi:
    teza = True
    last = "0"
    for i in ciag: 
        if last == i == '1':
            teza = False
            break
        last = i
    if teza:
        ilosc += 1
print("Zadanie 63.2")
print(f"Ilość ciągów: {ilosc}")


### 63.3
def sito_era(n):
    arr = [a for a in range(2, n+1)]
    for index, i in enumerate(arr):
        if i != 0:
            for y in range(index+i, len(arr), i):
                arr[y] = 0
    return [a for a in arr if a != 0]

ciagi = [int(i, 2) for i in ciagi] # zamiana na integery
najwieksza_ogolnie = max(ciagi) # największa liczba z pliku
pierwsze = sito_era(najwieksza_ogolnie//2 + 1)

ilosc = 0
maks = 0
mini = 99999999999999999
for i in ciagi:
    for y in pierwsze:
        if i/y == i//y and i//y in pierwsze:
            ilosc += 1
            if i > maks:
                maks = i
            elif i < mini:
                mini = i
            break

print("Zadanie 63.3")
print(f"Ilość: {ilosc}")
print(f"Max: {maks}")
print(f"Min: {mini}")

