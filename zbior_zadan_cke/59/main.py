#!/usr/bin/env python3
# 15.02.2022 by neloduka_sobe

# Wczytywanie danych
liczby = []
with open("dane/liczby.txt", "r") as f:
    for line in f:
        liczby.append(int(line.strip()))
    

### 59.1
def czynniki_pierwsze(n):
    czynniki = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            czynniki.add(d)
        d += 1
    if n > 1:
        czynniki.add(n)
    return czynniki


ilosc = 0
for i in liczby:
    czyn = czynniki_pierwsze(i)
    if len(czyn) == 3 and sum(czyn) % 2 != 0:
        ilosc += 1

print("Zadanie 59.1")
print(f"Ilość: {ilosc}")

### 59.2
def palindrom(n):
    s = n + int(str(n)[::-1])
    s = str(s)
    return s == s[::-1]

ilosc2 = 0
for i in liczby:
    if palindrom(i):
        ilosc2 += 1

print("Zadanie 59.2")
print(f"Ilość: {ilosc2}")


### 59.3
def moc_n(n, k=0):
    if len(str(n)) == 1:
        return k
    ilo = 1
    for i in str(n):
        ilo *= int(i)
    return moc_n(ilo, k+1)

moc = [0,0,0,0,0,0,0,0,0]
max1 = 0
min1 = 9999999999
for i in liczby:
    moc[moc_n(i)-1] += 1
    if moc_n(i ) == 1:
        if i < min1:
            min1 = i
        if i > max1:
            max1 = i

print("Zadanie 59.3")
for i in range(8):
    print(f"Ilość liczb o mocy {i+1}: {moc[i]}")
print(f"Max o mocy 1: {max1}")
print(f"Min o mocy 1: {min1}")
