#!/usr/bin/env python3
# 15.02.2022 by neloduka_sobe
import math

ciagi = []
with open('dane/ciagi.txt', 'r') as f:
    for line in f:
       ciag = line.strip().split(" ") 
       if len(ciag) == 1:
           continue
       else:
           ciag = [int(a) for a in ciag]
           ciagi.append(ciag)

bledne = []
with open('dane/bledne.txt', 'r') as f:
    for line in f:
       ciag = line.strip().split(" ") 
       if len(ciag) == 1:
           continue
       else:
           ciag = [int(a) for a in ciag]
           bledne.append(ciag)

### 61.1
ilosc = 100
max_roz = 0
for ciag in ciagi:
    arytm = True
    roznica = ciag[1] - ciag[0]
    for i in range(1, len(ciag)):
        if ciag[i] - ciag[i-1] != roznica:
            ilosc -= 1
            arytm = False
            break
    if roznica > max_roz and arytm:
        max_roz = roznica

print("Zadanie 61.1")
print(f"Ilość ciągów: {ilosc}")
print(f"Max różnica: {max_roz}")


### 61.2
print("Zadanie 61.2")
for ciag in ciagi:
    maks = 0 
    for i in ciag:
        if math.ceil(i**(1/3))**3 == i  and i > maks:
            maks = i
    if maks != 0:
        print(maks)

### 61.3
print("Zadanie 61.3")
for ciag in bledne:
    zle = set()
    for i in range(1,len(ciag)-1):
        if (ciag[i-1] + ciag[i+1])/2 != ciag[i]:
            zle.add(i)
    zle = sorted(list(zle))
    if len(zle) == 3:
        print(ciag[zle[1]])
    elif len(zle) == 1:
        print(ciag[0 if zle[0] == 1 else -1])
    elif len(zle) == 2:
        print(ciag[1 if zle[0] == 1 else -2])
