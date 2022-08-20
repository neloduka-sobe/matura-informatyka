#!/usr/bin/env python3

### Wczytywanie danych
dane = []

with open('dane/stopa_bezrobocia.txt', 'r') as f:
    for line in f:
        if line[0] == 'R':
            continue
        line = line.strip().split('\t')
        dane.append([int(line[0])] + [float(i.replace(',', '.')) for i in line[1:]])

### Zadanie 97.1
ilosc1 = 0
for i in dane:
    for y in i[1:]:
        if y > 10.0:
            ilosc1 += 1

print(f"Zadanie 97.1\n{ilosc1=}")

### Zadanie 97.2
max_war = 0
min_war = 999999999
max_ind = 0
min_ind = 0
for i in dane:
    y = round(sum(i[1:])/12, 2)
    if y > max_war:
        max_war = y
        max_ind = i[0]
    elif y < min_war:
        min_war = y
        min_ind = i[0]

print("Zadanie 97.2")
print(f"Max: {max_war}, Rok: {max_ind}")
print(f"Min: {min_war}, Rok: {min_ind}")

### Zadanie 97.3
with open("wykres_zad3.csv", "w") as f:
    f.write('Rok;Minimalne bezrobocie;Maksymalne bezrobocie\n')
    for i in dane:
        tmp = f"{i[0]};{min(i[1:])};{max(i[1:])}\n"
        f.write(tmp.replace('.',','))
print("Zadanie 97.3 w pliku wykres_zad3.csv")

### Zadanie 97.4
wyniki4 = dict()
dlugosc = 0
punkty = [[0,0],[0,0]]

last = 99999999
for i in dane:
    for y in i[1:]:
        if punkty[0] == [0,0]:
            punkty[0] = [i[0], i.index(y)]
            dlugosc += 1
        elif y <= last:
            dlugosc += 1
        elif y > last:
            punkty[1] = [i[0], i.index(y)-1] if i.index(y)-1 != 1 else [i[0]-1, 12]
            wyniki4[dlugosc] = punkty 
            dlugosc = 1
            punkty = [[0,0],[0,0]]
        last = y

print("Zadanie 97.4")
print(f"Długość: {max(wyniki4)}, Start/Stop (rok, miesiąc): {wyniki4[max(wyniki4)]}")

### Zadanie 97.5
ilosc = 0
last = [999999999 for y in range(12)]

for i in dane:
    teza = True
    for x, y in zip(i[1:], last):
        if not (x > y):
            teza = False

    last = i[1:]

    if teza:
        ilosc += 1


print(f"Zadanie 97.5\n{ilosc=}")
