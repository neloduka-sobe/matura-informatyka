#!/usr/bin/env python3

dane = []

with open('dane/punkty_rekrutacyjne.txt', 'r', encoding='iso-8859-1') as f:
    for line in f:
        if line[:8] == 'Nazwisko':
            continue
        line = line.strip().split(';')
        dane.append(line[:2] + [int(i) for i in line[2:]])

### Zadanie 89.1
uczniowie = []
for i in dane:
    if i[2] == 0 and i[3] >= 5 and (sum(i[4:8]))/4 > 4:
        uczniowie.append(i[:2])

print("Zadanie 89.1")
uczniowie = sorted(uczniowie, key=lambda x: x[0])
for i in uczniowie:
    print(*i)
    if uczniowie.index(i) == 4:
        break

### Zadani3 89.2

def punkty(tab):
    pkt = 0
    pkt += sum(tab[8:])/10
    for i in tab[4:8]:
        if i == 3: pkt += 4
        elif i == 4: pkt += 6
        elif i == 5: pkt += 8
        elif i == 6: pkt += 10
    if tab[3] == 6: pkt += 2
    pkt += tab[2]
    return pkt

pkt_uczniow = dict()
wynik2 = dict()
for i in dane:
    p = punkty(i)
    if p not in wynik2.keys():
        wynik2[p] = 1
    else:
        wynik2[p] += 1
    pkt_uczniow[' '.join(i[:2])] = p

print("\nZadanie 89.2")
print('Najczęstszy wynik:', max(wynik2, key=lambda x: wynik2[x]))
for i, y in pkt_uczniow.items():
    if y == max(wynik2, key=lambda x: wynik2[x]):
        print(i)

### Zadanie 89.3

print("\nZadanie 89.3")
for i in dane:
    if i[-5:].count(100) >= 3: 
        print(' '.join(i[:2]))

### Zadanie 89.4
oceny = {i: [0 for y in range(5)] for i in range(4)}
for i in dane:
    for ind, y in enumerate(i[4:8]):
        oceny[ind][y-2] += 1
        
print("\nZadanie 89.4 (wykres w plik wykres.ods)")
for i, naz in zip(oceny.keys(), ["Jezyk Polski", "Matematyka", "Biologia", "Geografia"]):
    print(f"{naz}: {oceny[i]}")

### Zadanie 89.5
def warunki_do_zad_5(tab):
    wyniki = 0
    pkt = 0

    wyniki += sum(tab[8:])/10
    for i in tab[4:8]:
        if i == 3: pkt += 4
        elif i == 4: pkt += 6
        elif i == 5: pkt += 8
        elif i == 6: pkt += 10
    pkt += tab[2]
    if tab[3] == 6: pkt += 2

    return pkt > wyniki
    
ilosc5 = 0
for i in dane:
    if warunki_do_zad_5(i):
        ilosc5 += 1

print(f'\nZadanie 89.5:\n{ilosc5=}')
