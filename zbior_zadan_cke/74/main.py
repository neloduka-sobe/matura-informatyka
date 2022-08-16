#!/usr/bin/env python3
import re

dane = []

with open('dane/hasla.txt', 'r') as f:
    for line in f:
        dane.append(line.strip())


### Zad 74.1
pattern = '^[0-9]+$'
ilosc1 = 0

for i in dane:
    if re.match(pattern, i):
        ilosc1 += 1

print("Zadanie 74.1")
print(f"{ilosc1=}")

### Zad 74.2
powtorzenia = dict()
for i in dane:
    if i in powtorzenia.keys():
        powtorzenia[i] += 1
    else:
        powtorzenia[i] = 1 

print("Zadanie 74.2")
print(sorted([i for i in powtorzenia.keys() if powtorzenia[i] > 1]))

### Zad 74.3

ilosc3 = 0
for i in dane:
    if len(i) >= 4:
        for y in range(3, len(i)):
            tmp = sorted(i[y-3:y+1])
            a,b,c,d = tmp
            if ord(a) + 1 == ord(b) and ord(b) + 1 == ord(c) and ord(c) + 1 == ord(d):
            # druga wersja # if ord(tmp[0]) - ord(tmp[1]) == -1 and ord(tmp[1])-ord(tmp[2]) == -1 and ord(tmp[2])-ord(tmp[3]) == -1:
                ilosc3 += 1
                break

print("Zadanie 74.3")
print(f"{ilosc3=}")

### Zad 74.4
ilosc4 = 0
for i in dane:
    pattern1 = '[a-z]+'
    pattern2 = '[A-Z]+'
    pattern3 = '[0-9]+'
    if re.search(pattern1, i) and re.search(pattern2, i) and re.search(pattern3, i):
        ilosc4 += 1
print("Zadanie 74.4")
print(f"{ilosc4=}")

