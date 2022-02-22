#!/usr/bin/env python3
# 21.02.2022 by neloduka_sobe

# Wczytywanie danych
dane = []
with open("dane/dane_ulamki.txt", "r") as f:
    for line in f:
        line = line.strip().split(" ")
        line = [int(a) for a in line]
        dane.append(line)

### 65.1
mini = 12001
min_mian = 12001
min_licz = 12001
for i in dane:
    if i[0]/i[1] < mini:
        min_mian = i[1]
        min_licz = i[0]
        mini = i[0]/i[1]
    elif i[0]/i[1] == mini and i[1] < min_mian:
        min_mian = i[1]
        min_licz = i[0]

print("Zadanie 65.1")
print(f"Licznik: {min_licz}; Mianownik: {min_mian}")

### 65.2
def nwd(a,b):
    while b != 0:
        b, a = a%b, b
    return a

licznik = 0
for i in dane:
    if nwd(i[1], i[0]) == 1:
        licznik += 1

print("Zadanie 65.2")
print(f"Ilość: {licznik}")

### 65.3
suma = 0
for i in dane:
    suma += i[0]/nwd(i[1], i[0])


print("Zadanie 65.3")
print(f"Suma: {suma}")

### 65.4
b = (2**2)*(3**2)*(5**2)*(7**2)*13
suma_licz = 0
for i in dane:
    suma_licz += (b*i[0])/(i[1])

print("Zadanie 65.4")
print(f"Licznik wynosi: {suma_licz}")
