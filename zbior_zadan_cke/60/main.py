#!/usr/bin/env python3
# 15.02.2022 by neloduka_sobe

# Wczytywanie danych
liczby = []
with open("dane/liczby.txt", "r") as f:
    for line in f:
        liczby.append(int(line.strip()))

### 60.1
mniejsze_od_1000 = []

for i in liczby:
    if i < 1000:
        mniejsze_od_1000.append(i)

print("Zadanie 60.1")
print(f"Ilość: {len(mniejsze_od_1000)}")
print(f"Ostatnie: {mniejsze_od_1000[-2:]}")

wszystkie_dziel = [] # do zad. 3
### 60.2
def dzielniki(n):
    dzielniki = [1,n]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            dzielniki.append(i)
            dzielniki.append(n//i)
    return dzielniki

print("Zadanie 60.2")
for i in liczby:
    dziel = dzielniki(i)

    # do zad. 3
    for j in dziel:
        wszystkie_dziel.append(j)

    if len(dziel) == 18:
        print(f"Liczba: {i}; dzielniki: {sorted(dziel)}")


### 60.3
maks = 0

for i in liczby:
    dziel = dzielniki(i)
    
    teza = True
    for j in dziel:
        if j == 1:
            continue

        if wszystkie_dziel.count(j) > 1:
            teza = False
            break
    if teza and i > maks:
        maks = i

print("Zadanie 60.3")
print(f"Max: {maks}")


