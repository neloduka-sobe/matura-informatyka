#!/usr/bin/env python3
# 9.03.2022 by neloduka_sobe

dane = []
with open("dane/dane_napisy.txt","r") as f:
    for line in f:
        line = line.strip().split(" ")
        dane.append(line)

### 68.1

ilosc1 = 0
for i in dane:
    if len(set(i[0])) == len(set(i[1])) == 1 and len(i[0]) == len(i[1]):
        ilosc1 += 1

print("Zadanie 68.1")
print(f"Ilość: {ilosc1}")


### 68.2

ilosc2 = 0
for i in dane:
    if ''.join(sorted(i[0])) == ''.join(sorted(i[1])):
        ilosc2 += 1

print("Zadanie 68.2")
print(f"Ilość: {ilosc2}")


### 68.3
anagramy = dict()

for i in dane:
    tmp0 = ''.join(sorted(i[0])) 
    tmp1 = ''.join(sorted(i[1])) 

    if tmp0 not in anagramy.keys():
        anagramy[tmp0] = 1
    elif tmp0 in anagramy.keys():
        anagramy[tmp0] += 1
    if tmp1 not in anagramy.keys():
        anagramy[tmp1] = 1
    elif tmp1 in anagramy.keys():
        anagramy[tmp1] += 1

print("Zadanie 68.3")
print(f"Maks: {max(anagramy.values())}")
