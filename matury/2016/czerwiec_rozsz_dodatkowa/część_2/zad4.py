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
print("4.2")
print(f"miejsce\tilość")
for i in sorted(d2.keys()):
	print(f"{i}\t{d2[i]}")

# 4.3
kwota_k = 25000
kwota_m = 30000

