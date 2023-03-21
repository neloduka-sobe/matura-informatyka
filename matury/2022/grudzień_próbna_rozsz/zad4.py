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

dzien_tyg = 4 # 0 - poniedziałek; 6 - niedziela
ilosc_dni_bez_opadow = 0

# 4.1
dlugosc_okresu = 0 # a)
pocz = '' # a)
koniec = '' # a)
ilosc_podlan = 0 # b)
okresy = [] # b)

# 4.2
retencja = {}

# 4.3
zbiornik = 5000
pobrana_woda_suma = 0
ilosc_pobran = 0

for i in dane:
	dzien_tyg = (dzien_tyg + 1) % 7
	nr_dnia = i[0][:2]
	nr_mies = i[0][3:5]
	if zbiornik < 0:
		ilosc_pobran += 1
		pobrana_woda_suma += abs(zbiornik)
		zbiornik = 0
	zbiornik += i[1]
	zbiornik -= 190
	
	if dzien_tyg == 2:
		zbiornik -= 70

	if i[1] == 0:
		ilosc_dni_bez_opadow += 1
	else:
		ilosc_dni_bez_opadow = 0
		
	# 4.1
	if int(nr_mies) in range(4,10):
		if ilosc_dni_bez_opadow % 5 == 0 and ilosc_dni_bez_opadow > 0:
			ilosc_podlan += 1	
			zbiornik -= 300 # 4.3

		if i[1] == 0:
			if dlugosc_okresu != 0:
				dlugosc_okresu += 1
				koniec = i[0]
			else:
				pocz = i[0]
				dlugosc_okresu = 1
		else:
			if dlugosc_okresu != 0:
				okresy.append((pocz, koniec, dlugosc_okresu))
				koniec = ''
				pocz = ''
				dlugosc_okresu = 0
				
	# 4.2
	retencja.setdefault(nr_mies, 0)
	retencja[nr_mies] += i[1]

# 4.1
print("Zadanie 4.1")
wynik = sorted(okresy, key=lambda x: x[2])[-1]
print(f"a) początek: {wynik[0]}; koniec: {wynik[1]}; długosc: {wynik[2]}")
print(f"b) {ilosc_podlan}")	

# 4.2
print("\nZadanie 4.2")
for i in retencja.keys():
	print(f"{i}\t{retencja[i]}")

# 4.3
print("\nZadanie 4.3")
print(f"a) {ilosc_pobran}")
print(f"b) {pobrana_woda_suma}")
