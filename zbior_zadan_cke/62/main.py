#!/usr/bin/env python3
# 16.02.2022 by neloduka_sobe

# Wczytywanie danych
liczby1 = []
with open("dane/liczby1.txt", 'r') as f:
    for line in f:
        liczby1.append(int(line.strip(),8))

liczby2 = []
with open("dane/liczby2.txt", 'r') as f:
    for line in f:
        liczby2.append(int(line.strip()))

### 62.1
print("Zadanie 62.1")
print(f"Max: {oct(max(liczby1))}")
print(f"Min: {oct(min(liczby1))}")


### 62.2
ciagi = []
w_trakcie = False
for i in range(1, len(liczby2)):
    if liczby2[i-1] <= liczby2[i] and not w_trakcie:
       pocz = liczby2[i-1] 
       dlugosc = 2
       w_trakcie = True
    elif liczby2[i-1] <= liczby2[i] and w_trakcie:
        dlugosc += 1
    elif w_trakcie:
        w_trakcie = False
        ciagi.append([pocz, dlugosc])
maks = max([i[1] for i in ciagi])
for i in ciagi:
    if i[1] == maks:
        print("Zadanie 62.2")
        print(f"Liczba: {i[0]}; długość: {i[1]}")

### Zad 62.3
ppa = 0
ppb = 0

for i in range(len(liczby1)):
    if liczby1[i] == liczby2[i]:
        ppa += 1
    if liczby1[i] > liczby2[i]:
        ppb += 1

print("Zadanie 62.3")
print(f"Ilość dla podpunktu a: {ppa}")
print(f"Ilość dla podpunktu b: {ppb}")

### Zad 62.4
ilosc_zap_10 = 0
ilosc_zap_8 = 0

for i in liczby2:
    ilosc_zap_10 += str(i).count('6')
    ilosc_zap_8 += str(oct(i)).count('6')

print("Zadanie 62.4")
print(f"Zapis dziesiętny: {ilosc_zap_10}")
print(f"Zapis ósemkowy: {ilosc_zap_8}")
