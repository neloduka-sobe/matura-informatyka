#!/usr/bin/env python3
with open("dane/gpw.txt", "r") as f:
    dane = [line.strip().split("\t") for line in f]

### 95.1
maks = dict()
for i in dane:
    if i[0] == '2015-01-21':
        maks[float(i[3].replace(',','.')) if int(i[4]) == int(i[5]) == 0 else int(i[5]) / int(i[4])] = i[1]

print("Zadanie 95.1")
print(*[f"{round(y, 2)} {maks[y]}" for y in sorted(maks.keys(), reverse = True)[:3]], sep = '\n')

### 95.2
spolki = set()
for i in dane:
    spolki.add(i[1])

nazwa = ''
wartosc = 0
for y in spolki:
    kz1 = 0
    kz2 = 0
    for z in dane:
        if z[1] == y:
            if z[0] == '2015-01-22':
                kz1 = float(z[3].replace(',','.'))
            elif z[0] == '2015-01-23':
                kz2 = float(z[3].replace(',','.'))
                d = ((kz2/kz1)-1)*100
                if d > wartosc:
                    nazwa = z[1]
                    wartosc = d

print("Zadanie 95.2")
print(f"Nazwa: {nazwa}")
print(f"Wartosc: {round(wartosc,2)}")


### 95.3
zag = 0
ob_zag = 0
kraj = 0
ob_kraj = 0
for i in dane:
    if i[2][:2] == "PL":
        kraj += 1
        ob_kraj += int(i[5])
    else:
        zag += 1
        ob_zag += int(i[5])

print("Zadanie 95.3")
print("(a)")
print(f"Krajowe: {kraj//3}")
print(f"Obrót: {ob_kraj}")
print(f"Zagraniczne: {zag//3}")
print(f"Obrót: {ob_zag}")
print(f"Proc. udział spk.: {round(ob_kraj/(ob_kraj+ob_zag)*100, 2)}")

### 95.4
daty = ['2015-01-21', '2015-01-22', '2015-01-23']
m = dict()
for da in daty:
    if da not in m.keys():
        m[da] = 0
    for i in dane:
        if da == i[0]:
            m[da] = m[da] + float(i[3].replace(',','.')) * int(i[6])

print("Zadanie 95.4")
for i in daty:
    print("data", "wig", "m")
    print(i, round((m[i])/(57140000*96.48213739) * 1000, 2), m[i])


### 95.5
kursy = dict()
for i in spolki:
    kursy[i] = [0,0,0]

for i in dane:
    if i[0] == daty[0]:
        kursy[i[1]][0] = i[3]
    elif i[0] == daty[1]:
        kursy[i[1]][1] = i[3]
    elif i[0] == daty[2]:
        kursy[i[1]][2] = i[3]

kupic = 0
sprzedac = 0
czekac = 0
for i in kursy.keys():
    if float(kursy[i][1].replace(',','.')) - float(kursy[i][0].replace(',','.')) < float(kursy[i][2].replace(',','.')) - float(kursy[i][1].replace(',','.')) and float(kursy[i][1].replace(',','.')) - float(kursy[i][0].replace(',','.')) > 0:
        kupic += 1
    elif float(kursy[i][1].replace(',','.')) - float(kursy[i][0].replace(',','.')) > float(kursy[i][2].replace(',','.')) - float(kursy[i][1].replace(',','.')) and float(kursy[i][1].replace(',','.')) - float(kursy[i][0].replace(',','.')) < 0:
        sprzedac += 1
    else:
        czekac += 1

print("Zadanie 95.5")
print(f"Kupic: {kupic}")
print(f"Sprzedac: {sprzedac}")
print(f"Czekac: {czekac}")
