#!/usr/bin/env python3
#13.05.2022 by neloduka_sobe

# Wczytywanie danych
dane = [int(i) for i in open('dane/dane_trojkaty.txt')]

### 80.1
def prostokatne(a,b,c):
    return a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2

print("Zadanie 80.1")
for i in range(2, 500):
    if prostokatne(dane[i], dane[i-1], dane[i-2]):
        print(dane[i-2], dane[i-1], dane[i])

### 80.2
max1 = 0
def da_sie_troj(a,b,c):
    return a + b > c and a + c > b and b + c > a

### Gorsza wersja
'''
for x in range(500):
    for y in range(x+1, 500):
        for i in range(y+1, 500):
            if da_sie_troj(dane[x], dane[y], dane[i]) and x != y and y != i:
                ile = (sum([dane[x], dane[y], dane[i]]))
                if ile > max1:
                    max1 = ile

print(f"Zadanie 80.2: {max1}")
'''

### Lepsza wersja
dane1 = sorted(dane)
dane1.reverse()
obw = 0

for i in range(2, 500):
    if da_sie_troj(dane1[i], dane1[i-1], dane1[i-2]):
        obw = dane1[i] + dane1[i-1] + dane1[i-2]
        print(f"Zadanie 80.2: {obw}")
        break


### 80.3

### Gorsza wersja
'''
ilosc = 0

for x in range(500):
    for y in range(x+1, 500):
        for i in range(y+1, 500):
            if da_sie_troj(dane[x],dane[y],dane[i]):
                ilosc += 1

print(f"Zadanie 80.3: {ilosc}")
'''

### Lepsza wersja
ilosc = 0

for x in range(500):
    for y in range(x+1, 500):
        for i in range(y+1, 500):
            if da_sie_troj(dane1[x], dane1[y], dane1[i]):
               ilosc += 1 
            else:
                break

print(f"Zadanie 80.3: {ilosc}")
