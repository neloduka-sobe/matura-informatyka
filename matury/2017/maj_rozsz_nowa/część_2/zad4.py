#!/usr/bin/env python3
from math import ceil
cukier = []
cennik = {}
with open('Dane_PR/cukier.txt','r') as f:
	for i in f:
		i = i.strip().split()
		i[2] = int(i[2])
		cukier.append(i)

with open('Dane_PR/cennik.txt','r') as f:
	for i in f:
		i = i.strip().split()
		i[1] = float(i[1].replace(',','.'))
		cennik[i[0]] = i[1]

# 4.1
d1 = {}
for i in cukier:
	d1.setdefault(i[1],0)
	d1[i[1]] += i[2]

nazwy = sorted(d1, key=lambda x: d1[x])[-3:]
print("4.1")
for i in nazwy:
	print(f"NIP: {i}; Ilość: {d1[i]} ")

# 4.2
suma = {}
for i in cukier:
	rok = i[0][:4]
	suma.setdefault(rok,0)
	suma[rok] += (i[2] * cennik[rok])
print("\n4.2")
print("Rok; Przychód")
for i in suma:
	print(f"{i}; {round(suma[i],2)}")

# 4.3
d3 = {}

for i in cukier:
	rok = i[0][:4]
	d3.setdefault(rok,0)
	d3[rok] += i[2]

with open('wykres.csv','w') as f:
	f.write("Rok; Ilość sprzedanego cukru\n")
	for i in d3:
		f.write(f"{i}; {d3[i]}\n")
		
print("\n4.3 w pliku wykres.csv/wykres.ods")

# 4.4
d4 = {}
suma_rab = 0
for i in cukier:
	nip = i[1]
	d4.setdefault(nip,0)
	d4[nip] += i[2]

	tmp = d4[nip]
	if 100 <= tmp < 1000:
		suma_rab += (i[2]*0.05)
	elif 1000 <= tmp < 10000:
		suma_rab += (i[2]*0.1)
	elif 10000 <= tmp:
		suma_rab += (i[2]*0.2)

print(f"\n4.4: {round(suma_rab,2)}")

# 4.5
c = 5000
ile5 = 0
for ind,i in enumerate(cukier):
	if ind == len(cukier)-1 or (int(i[0][-2:]) > int(cukier[ind+1][0][-2:])):
		if c < 5000:
			tmp = 5000 - c
			tmp /= 1000
			tmp = ceil(tmp)	
			tmp *= 1000
			if tmp >= 4000:
				ile5 += 1
			c += tmp
	c -= i[2]

print(f"\n4.5: {ile5}")
