#!/usr/bin/env python3

### Wczytywanie danych
dane = []

with open('dane/dane_wybory.txt', 'r') as f:
    for line in f:
        dane.append(line.strip().split(' '))

### Funkcje
def wk(gk, mk):
    return (gk)/(2*mk + 1)

### Zadanie 86.1
with open('wykres.csv', 'w') as f:
    f.write('')

print("Zadanie 86.1")
for i in dane:
    with open('wykres.csv', 'a') as f:
        print(f"Okręg: {i[0]}; Suma głosów: {sum([ int(a) for a in i[1:]])}")
        f.write(f"{i[0]},{sum([ int(a) for a in i[1:]])}\n")


### Zadanie 86.2

proc = dict()

for i in dane:
    proc[i[0]] = [round((int(b)/sum([ int(a) for a in i[1:]])),2) for b in i[1:]]

print("Zadanie 86.2")
for i in range(5):
    print(f"K{i}: {max(proc, key=lambda x: proc[x][i])}")

### Zadanie 86.3
wyniki3 = []

for i in dane:
    mandaty = {f'K{i}':0 for i in range(1, 6)}
    for y in range(20):
        wartosci = [wk(int(i[a]), mandaty[f"K{a}"] ) for a in range(1,6)]
        ind = wartosci.index(max(wartosci)) + 1
        mandaty[f'K{ind}'] += 1
    wyniki3.append([int(i) for i in mandaty.values()])

print("Zadanie 86.3")
for i in range(5):
    print(f"K{i+1}: {max(wyniki3, key=lambda x: int(x[i]))[i]}")

### Zadanie 86.4

# Standardowy
print("Zadanie 86.4 standardowy")
suma = [0 for i in range(5)]
for x in wyniki3:
    for y in range(5):
        suma[y] += x[y]

for i in range(5):
    print(f"K{i}: {suma[i]}")

# Regionalny
dane_reg = [dane[line:line+5] for line in range(0,len(dane), 5)]
dane_reg = [[sum([int(i[z][y]) for z in range(len(i))]) for y in range(1, len(i[0]))] for i in dane_reg]

wyniki4 = []

for i in dane_reg:
    mandaty = {f'K{i}':0 for i in range(1, 6)}
    for y in range(100):
        wartosci = [wk(int(i[a-1]), mandaty[f"K{a}"]) for a in range(1,6)]
        ind = wartosci.index(max(wartosci)) + 1
        mandaty[f'K{ind}'] += 1
    wyniki4.append([int(i) for i in mandaty.values()])

print("Zadanie 86.4 regionalny")
suma = [0 for i in range(5)]
for x in wyniki4:
    for y in range(5):
        suma[y] += x[y]

for i in range(5):
    print(f"K{i}: {suma[i]}")


### Zadanie 86.5
print("Zdanie 86.5")
m = [10, 20, 50]
ilosc = 100000
for mx in m:
    for Q in range(1, ilosc//2 + 1):
        Mm = 0
        Qm = 0
        M = ilosc - Q
        for i in range(2*mx):
            if wk(Q, Qm) >= wk(M, Mm) :
                Qm += 1
            else:
                Mm += 1

        if Qm == mx:
            print(f'{mx=}: {Q}')
            break
