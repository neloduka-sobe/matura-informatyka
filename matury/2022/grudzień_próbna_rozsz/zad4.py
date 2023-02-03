#!/usr/bin/env python3
dane = []

### Wczytywanie danych
with open('Dane/ekodom.txt', 'r') as f:
    for ind, i in enumerate(f):

        # Pomijanie opisu kolumn
        if ind == 0:
            continue
        i = i.strip().split('\t')
        i[1] = int(i[1])
        dane.append(i)

print(dane)

### 4.1
dl_ciagu = 0
dni = []
dzien_tyg = 6

for i in dane:

    # Aktualizowanie dnia tygodnia
    dzien_tyg += 1
    if dzien_tyg == 8:
        dzien_tyg = 1
    
    if i[0] != 0:
        if dl_ciagu == 0:
            dl_ciagu = 1
        else:
            dl_ciagu += 1
    elif i[0] == 0:
            if dl
