#!/usr/bin/env python3

dane = []

### Wczytywanie danych
# rok wiek m_miasto k_miasto m_wies k_wies
with open('dane/ludnosc.txt', 'r') as f:
    for line in f:
        if line[0] == 'r':
            continue
        dane.append([int(i) for i in line.strip().split('\t')])

### Zadanie 96.1

w2013 = {} 
w2050 = {} 
for i in dane:
    if i[0] == 2013:
        w2013[i[1]] = sum(i[2:])
    elif i[0] == 2050:
        w2050[i[1]] = sum(i[2:])

print("Zadanie 96.1 w pliku wykres.csv")
with open('wykres.csv', 'w') as f:
    f.write('Wiek,Rok 2013,Rok 2050\n')
    for i in range(101):
        f.write(f'{i},{w2013[i]},{w2050[i]}\n')

### Zadanie 96.2

zad2_2013 = [0,0]
zad2_2050 = [0,0]
for i in dane:
    if i[0] == 2013:
        zad2_2013[0] += sum(i[2:4])
        zad2_2013[1] += sum(i[4:])
    elif i[0] == 2050:
        zad2_2050[0] += sum(i[2:4])
        zad2_2050[1] += sum(i[4:])

print("Zadanie 96.2")
print(f"2013: {round(zad2_2013[0]/zad2_2013[1],2)}")
print(f"2050: {round(zad2_2050[0]/zad2_2050[1],2)}")

### Zadanie 96.3
licznik_2013 = 0
mianownik_2013 = 0

licznik_2050 = 0
mianownik_2050 = 0

for i in dane:
    if i[0] == 2013:
        mianownik_2013 += i[2]
        licznik_2013 += (i[1] * i[2])
    elif i[0] == 2050:
        mianownik_2050 += i[2]
        licznik_2050 += (i[1] * i[2])

print("Zadanie 96.3")
print(f"2013: {round(licznik_2013/mianownik_2013)}")
print(f"2050: {round(licznik_2050/mianownik_2050)}")

### Zadanie 96.4
wiek_per_rok = {i: 0 for i in range(2013, 2051)}

for i in dane:
    if wiek_per_rok[i[0]] != 0:
        continue

    if (i[2] + i[4]) < (i[3] + i[5]):
        wiek_per_rok[i[0]] = i[1]

print("Zadanie 96.4")
for i in wiek_per_rok.keys():
    print(f"Rok: {i}, wiek: {wiek_per_rok[i]}")

### Zadanie 96.5
zad5 = {i: [0,0,0] for i in range(2013, 2051)}

for i in dane:
    if i[1] <= 18:
        zad5[i[0]][0] += sum(i[3:]) 
    elif i[1] in range(19, 68):
        zad5[i[0]][1] += sum(i[3:])
    elif i[1] > 67:
        zad5[i[0]][2] += sum(i[3:])

with open('wykres_zad5.csv', 'w') as f:
    f.write('Rok,Mlodziez,Osoby w wieku produkcyjnym,Emeryci\n')
    for i in zad5.keys():
        f.write(f'{i},{zad5[i][0]},{zad5[i][1]},{zad5[i][2]}\n')

print("Zadanie 96.5 b) (część b) w pliku wykres_zad5.csv)")
for i in zad5.keys():
    print(f'Rok: {i}, Procent osób w wieku produkcyjnym: {round((zad5[i][1]/sum(zad5[i]))*100)}%')
