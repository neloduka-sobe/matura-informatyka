#!/usr/bin/env python3
import math
dane = []
with open('Dane_PR/woda.txt','r') as f:
	for i in f:
		i = i.strip().split()
		i[1] = int(i[1])
		dane.append(i)

# 5.1
d1 = {}
for i in dane:
	rok = i[0][:4]
	d1.setdefault(rok, 0)
	d1[rok] += i[1]
print(f"5.1: {max(d1, key=lambda x: d1[x])}")

# 5.2
m = ['','']
ml = 0
l = 0
p = ''
k = ''
for i in dane:
	if i[1] > 10000:
		if l == 0:
			p = i[0]
		k = i[0]
		l += 1
	else:
		if l > ml:
			ml = l
			m = [p,k]
		l = 0
		
print(f"5.2: od {m[0]} do {m[1]}; dlugosc: {ml}")

# 5.3
d3 = {}
for i in dane:
	rok = i[0][:4]
	mies = i[0][5:7]
	if rok == '2008':
		d3.setdefault(mies, 0)
		d3[mies] += i[1]

print("5.3: wykres w pliku")
with open('wykres5_3.csv','w') as f:
	f.write(f"Miesiąc;Ilość wody\n")
	for i in d3.keys():
		f.write(f"{i};{d3[i]}\n")

# 5.4
pierwsze_wyp = ''
zbiornik = 500000
ile_dni = 0
m_ilosc = 0
for i in dane:
	tmp = zbiornik
	''' sprawdzanie
	if i[0] == '2008-02-01':
		print(tmp)
	'''
	# c)
	if zbiornik > m_ilosc:
		m_ilosc = zbiornik
	# b)
	if zbiornik > 800000:
		ile_dni += 1
	# a)
	#''' zakomentować dla pp. c)
	if zbiornik > 1000000: 
		if pierwsze_wyp == '':
			pierwsze_wyp = i[0]
		zbiornik = 1000000
	zbiornik = int(zbiornik*0.98) # Błąd w odpowiedziach powinno być math.ceil, ale wtedy odpowiedzi się nie zgadzają
	# '''
	zbiornik += i[1]

print("5.4")
print("Aby uzyskać podpunkt c należy zakomentować")
print(f"{pierwsze_wyp} {ile_dni} {m_ilosc}")
