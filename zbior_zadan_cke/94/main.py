#!/usr/bin/env python3

### Wczytywanie danych
dane = []

with open("dane/wzrost.txt", "r") as f:
    for line in f:
        if line[0] == 'I':
            continue
        line = line.strip().split(';')
        line = [int(line[0]), line[1]] + [int(i) for i in line[2:]]
        dane.append(line)

### Zadanie 94.1
przyrost = dict()
for i in dane:
    p = (i[-1] - i[2]) / (i[2])
    przyrost[i[0]] = p

print("Zadanie 94.1")
print(f"id: {max(przyrost, key=lambda x: przyrost[x])}, Stosunek: {round(przyrost[max(przyrost, key=lambda x: przyrost[x])]*100)}%")

### Zadanie 94.2
sr_ch = {i: [0,0] for i in range(20)} 
sr_dz = {i: [0,0] for i in range(20)} 


for i in dane:
    for ind, y in enumerate(i[2:]):
        if i[1] == 'ch':
            sr_ch[ind][0] += y
            sr_ch[ind][1] += 1
        elif i[1] == 'd':
            sr_dz[ind][0] += y
            sr_dz[ind][1] += 1

print("\nZadanie 94.2")
for i in range(20):
    if ((sr_ch[i][0]/sr_ch[i][1]) - (sr_dz[i][0]/sr_dz[i][1])) <= -1:
        print(f"{i} lat")

### Zadanie 94.3
ilosc3 = 0
for i in dane:
    if i[17] >= i[18] >= i[19] >= i[20] >= i[21]:
        ilosc3 += 1

print(f"\nZadanie 94.3\n{ilosc3=}")

### Zadanie 94.4
print("\nZadanie 94.4")
for i in range(1, 20):
    print(f"Chłopcy. Wiek: {i} Przyrost: {(sr_ch[i][0]-sr_ch[i-1][0])/sr_ch[i][1]}")
    print(f"Dziewczyny. Wiek: {i} Przyrost: {(sr_dz[i][0]-sr_dz[i-1][0])/sr_dz[i][1]}")

print("\nZ obserwacji wyników:\nChłopcy: 11 lat\nDziewczyny: 8 lat")

### Zadanie 94.5
with open('centyle.csv', 'w') as f:
    for i in dane:
        if i[1] == 'ch':
            f.write(f"{i[3]};{i[12]};{i[-1]}\n")
print("\nZadanie 94.5\nDane do arkusza kalkulacyjnego w pliku centyle.csv")

### Zadanie 94.6
ilosc_ch = 0
for i in dane:
    if i[1] == 'ch':
        ilosc_ch += 1

print("\nZadanie 94.6")
with open('mediana.csv', 'w') as f:
    f.write("Wiek;Mediana\n")
    for z in range(2,len(dane[0])):
        id_ch = 1
        for i in sorted(dane, key=lambda x: x[z]):
            if i[1] == 'ch':
                if id_ch == int(ilosc_ch/2)+1:
                    print(f"Wiek: {z-2}, Mediana: {i[z]}")
                    f.write(f'{z-2};{i[z]}\n')

                id_ch += 1
print("Dane do wykresu w pliku mediana.csv")
