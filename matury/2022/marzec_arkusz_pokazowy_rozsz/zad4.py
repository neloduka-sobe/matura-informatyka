#!/usr/bin/env python3

dane = []

with open('Dane/brenna.txt', 'r') as f:
	for i in f:
		if i.startswith('data'):
			continue
		i = i.strip().split('\t')
		i[1] = float(i[1])
		i[2] = float(i[2])
		dane.append(i)
		
# 4.1
d = {}
for i in dane:
	data = i[0][:-6]
	d.setdefault(data, [])
	d[data] = d[data] + [i[1]]
	
print("4.1")
t = max(d, key=lambda x: max(d[x]) - min(d[x]))
print(f"{t}: {max(d[t]) - min(d[t])}")

# 4.2
d2 = {}
for i in dane:
	godz = i[0][-5:]
	d2.setdefault(godz, [0,0])
	d2[godz] = [d2[godz][0] + 1, d2[godz][1] + i[1]]

with open('wykres.csv', 'w') as f:
	for i in d2.keys():
		f.write(f"{i}; {round(d2[i][1]/d2[i][0], 2)}\n")
	
# 4.3
pocz = ''
kon = ''
suma = 0
l = 0
m_l = 0
m_pocz =  ''
m_kon = ''
m_suma = 0
for i in dane:
	if i[1] > 0 and i[2] > 0:
		if l != 0:
			l += 1
			suma += i[2]
			kon = i[0]
		else:
			l = 1
			suma += i[2]
			pocz = i[0]
	else:
		if l > m_l:
			m_pocz = pocz
			m_kon = kon
			m_l = l
			m_suma = suma
		pocz,kon,l,suma = '','',0,0
print("\n4.3")
print(f"dlugosc: {m_l} od  {m_pocz} do  {m_kon} ilosc: {round(m_suma,2)}")

# 4.4
ods = 0
snieg = 0
o = False
d4 = {}
for i in dane:
	if i[1] <= 0 and i[2] > 0:
		if o:
			o = False
			continue
		snieg += i[2]
	elif i[1] > 0 and i[2] > 0:
		snieg = 0

	if snieg >= 4:
		ods += 1
		d4.setdefault(i[0][:-6],0)
		d4[i[0][:-6]] += 1
		snieg = 0
		o = True
			
print("\n4.4")
print(f"a) {ods}")
m = max(d4, key=lambda x: d4[x])
print(f"b) {d4[m]} razy {m}")

