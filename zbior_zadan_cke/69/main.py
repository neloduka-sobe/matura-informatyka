#!/usr/bin/env python3

dane = []

with open('dane/dane_geny.txt', 'r') as f:
    for line in f:
        dane.append(line.strip())


### Zadanie 69.1
zad1 = dict()

for i in dane:
    if len(i) in zad1.keys():
        zad1[len(i)] += 1
    else:
        zad1[len(i)] = 1

max1 = 0
for i in zad1.keys():
    if zad1[i] > max1:
        max1 = zad1[i]

print("Zadanie 69.1")
print(f"Rozmiar największego gatunku: {max1=}")
print(f"Liczba gatunków: {len(zad1)=}")


### Zadanie 69.2

def usun_niekodujace(genotyp):
    ''' Usuwa niekodujące fragmenty z genotypu ''' 
    ret = []
    while genotyp.find("AA") != -1 and genotyp.find("BB") != -1:
        ret.append(genotyp[genotyp.index('AA'):genotyp.index('BB')+2])
        genotyp = genotyp[genotyp.index("BB")+2:]
    return ''.join(ret), [i for i in ret if i != '']


ilosc2 = 0
for i in dane:
    if usun_niekodujace(i)[0].find("BCDDC") != -1:
        ilosc2 += 1

print(f"Zadanie 69.2\n{ilosc2=}")

### Zadanie 69.3
max_il = 0
max_len = 0

for i in dane:
    i = usun_niekodujace(i)[1]
    if len(i) > max_il:
        max_il = len(i)

    if len(max(i, key=lambda x: len(x))) > max_len:
        max_len = len(max(i, key=lambda x: len(x)))

print(f"Zadanie 69.3\nMaksymalna ilość: {max_il=}, Maksymalna długość: {max_len=}")


### Zadanie 69.4
odporne = 0
silnie_odporne = 0

for i in dane:
    if i == i[::-1]:
        silnie_odporne += 1

    if usun_niekodujace(i[::-1])[0] == usun_niekodujace(i)[0]:
        odporne += 1


print(f"Zadanie 69.4\n{odporne=}, {silnie_odporne=}")
