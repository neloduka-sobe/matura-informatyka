#!/usr/bin/env python3
spol = ['A', 'E', 'I', 'O', 'U', 'Y'] # Tablica ze spółŋłoskami

# Wczytywanie danych
f = open("dane/tekst.txt", 'r')
dane =  f.readline().strip().split(" ")

### 73.1
ilosc = 0
for i in dane:
    last = ''
    for y in i:
        if y == last:
            ilosc += 1
            break
        last = y

print("Zadanie 73.1")
print(f"Ilość: {ilosc}")

### 73.2
slow = dict()

for z in dane:
    for j in z:
        if j not in slow.keys():
            slow[j] = 1
        else:
            slow[j] = slow[j] + 1

print("Zadnanie 73.2")
for k in sorted(slow.keys()):
    print(k, slow[k], round(slow[k]/sum([len(a) for a in dane])*100, 2))


### 73.3
dlu = 0
ilosc2 = 0
slowo = ''

for i in dane:
    dlug = 0
    for y in i:
        if y not in spol:
            dlug += 1
        else:
            if dlug > dlu:
                ilosc2 = 1
                dlu = dlug
                slowo = i
            elif dlug == dlu:
                ilosc2 += 1
            dlug = 0
print("Zadanie 73.3")
print(f"{dlu=}")
print(f"{ilosc2=}")
print(f"{slowo=}")
