#!/usr/bin/env python3

dane = []

with open('NM_DANE_PR/pomiary.txt', 'r') as f:
	for i in f:
		if i.startswith('data;godzina;czujnik1;czujnik2;czujnik3;czujnik4;czujnik5;czujnik6;czujnik7;czujnik8;czujnik9;czujnik10'):
			continue
		dane.append(i.strip().split(';'))
# 5.1
ilosc_pomiarow1 = 0
suma1 = 0
for i in dane:
	if 5 <= int(i[1][:2]) <= 12:
		if int(i[1][:2]) == 12 and int(i[1][3:]) != 0:
			continue
		suma1 += float(i[6].replace(',','.'))
		ilosc_pomiarow1 += 1

print(f"5.1: {round((suma1/ilosc_pomiarow1),2)}")

# 5.2
d = [{} for i in range(10)]
with open('5_2.txt','w') as f:
	for i in dane:
		t = ''
		for ind,y in enumerate(i):
			if ind in (1,0):
				continue
			wartosc = int(273.15+float(y.replace(',','.')))
			d[ind-2].setdefault(wartosc, 0)
			d[ind-2][wartosc] += 1
			t += str(wartosc) + ' '
		f.write(f'{t}\n')

print("\n5.2")
for ind,i in enumerate(d):
	print(ind+1, max(i, key=lambda x: i[x]))

# 5.3

d3 = {}
for i in dane:
	if i[0][:4] != '2016':
		continue
	mies = i[0][5:7]
	d3.setdefault(mies,[0,0])
	d3[mies] = [d3[mies][0] + float(i[-1].replace(',','.')),  d3[mies][1]+1]

with open('wykres.csv','w') as f:
	f.write('Miesiąc;Średnia temperatura\n')
	for i in d3.keys():
		f.write(f"{i}; {round(d3[i][0]/d3[i][1],2)}\n")

# 5.4
p1 = 0
p2 = 0
for i in dane:
		for ind,y in enumerate(i):
			if ind in (1,0):
				continue
			w = float(y.replace(',','.'))
			if -10 < w <= 15:
				p1 += 1
			elif 15 < w <= 20:
				p2 += 1

print("5.4")
print(f"przedział 1.: {p1}; przedział 2.: {p2}")
