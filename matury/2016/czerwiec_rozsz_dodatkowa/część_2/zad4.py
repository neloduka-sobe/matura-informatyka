#!/usr/bin/env python3

dane = []
with open('MIN-R2A1P-163_dane/ubezpieczenia.txt','r') as f:
	for i in f:
		if i.startswith("Nazwisko;Imie;Data_urodz;Miejsce_zamieszkania"):
			continue
		i = i.strip().split(';')
		dane.append(i)

# 4.1
d = {}
for i in dane:
	data = i[2].strip()
	mies = data[5:7].strip()
	d.setdefault(mies, 0)
	d[mies] += 1

print("4.1")
print(f"miesiąc\tilość")
for i in sorted(d.keys()):
	print(f"{i}\t{d[i]}")
	

# 4.2
d2 = {}
for i in dane:
	miejsce = i[3].strip()
	if i[1].strip().endswith('a'):
		d2.setdefault(miejsce, 0)
		d2[miejsce] += 1
print("\n4.2")
print(f"miejsce\tilość")
for i in sorted(d2.keys()):
	print(f"{i}\t{d2[i]}")

# 4.3
kwota_k = 25000
kwota_m = 30000

sm = 0
sk = 0
for i in dane:
	wiek = 2016 - int(i[2][:4])
	plec = 'K' if i[1][-1] == 'a' else 'M'
	if wiek <= 30:
		if plec == 'K':
			sk += kwota_k * 0.001
		else:
			sm += kwota_m * 0.001
	elif 31 <= wiek <= 45:
		if plec == 'K':
			sk += kwota_k * 0.0015
		else:
			sm += kwota_m * 0.0015
	elif wiek >= 46:
		if plec == 'K':
			sk += kwota_k * 0.0012
		else:
			sm += kwota_m * 0.0012
	if wiek > 60:
		if plec == 'K':
			sk += 49
		else:
			sm += 49
			
print("\n4.3")
print(f"Mężczyźni: {round(sm,2)}; Kobiety: {round(sk,2)}")


# 4.4
d4 = {}
for i in dane:
	wiek = 2016 - int(i[2][:4])
	dekada = str(wiek)[0]
	d4.setdefault(dekada, 0)
	d4[dekada] += 1

print("\n4.4 w pliku")
with open('wykres.csv', 'w') as f:
	f.write("Przedział wiekowy;Ilosć\n")
	for i in d4.keys():
		f.write(f"{i}0-{i}9;{d4[i]}\n")
	
