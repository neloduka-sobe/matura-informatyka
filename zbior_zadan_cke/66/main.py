#!/usr/bin/env python3
# 22.02.2022 by neloduka_sobe

# Wczytywanie danych
dane = []
with open("dane/trojki.txt", "r") as f:
    for line in f:
        line = line.strip().split(" ")
        line = [int(a) for a in line]
        dane.append(line)


### 66.1
print("Zadanie 66.1")
suma = lambda a: sum([int(b) for b in str(a)])
ilosc1 = 0
for i in dane:
    if suma(i[0]) + suma(i[1]) == i[2]:
        print(i[0], i[1], i[2])
        ilosc1 += 1

print(f"Ilość: {ilosc1}")

### 66.2
def is_prime(a):
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

print("Zadanie 66.2")
ilosc2 = 0
for i in dane:
    if i[0] * i[1] == i[2]:
        if is_prime(i[0]) and is_prime(i[1]):
            print(i[0], i[1], i[2])
            ilosc2 += 1
print(f"Ilość: {ilosc2}")


### 66.3
def prostokatne(arr):
    a,b,c = arr
    return a**2 + b ** 2 == c**2

print("Zadanie 66.3")
last_b = False
last = [0,0,0]
for i in dane:
    pros = prostokatne(sorted([i[0], i[1], i[2]]))
    if pros:
        if not last_b:
            last_b = True
            last = [i[0], i[1], i[2]]
        else:
            print(last)
            print([i[0], i[1], i[2]])
            print()
    else:
        last_b = False

### 66.4
def trojkatny(arr):
    a,b,c = arr
    return a + b > c and c + b > a and a + c > b 

ilosc3 = 0
dlugosc = 0
maks = 0
for i in dane:
    if trojkatny(i):
        dlugosc += 1
        ilosc3 += 1
    else:
        if dlugosc > maks:
            maks = dlugosc
        dlugosc = 0


print("Zadanie 66.4")
print(f"Ilość: {ilosc3}")
print(f"Dlugosc: {maks}")
