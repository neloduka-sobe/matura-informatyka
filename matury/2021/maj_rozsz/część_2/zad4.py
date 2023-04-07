#!/usr/bin/env python3


dane = []
with open('DANE_2105/instrukcje.txt', 'r') as f:
	for i in f:
		dane.append(i.strip().split())

napis = []
rodzaj = ''
dl = 0
mdl = 0
mrodzaj = ''
d = {}
for i in dane:
	if i[0] == rodzaj:
		dl += 1
	else:
		if dl > mdl:
			mrodzaj = rodzaj
			mdl = dl
		rodzaj = i[0]
		dl = 1
	
	
	if i[0] == "DOPISZ":
		d.setdefault(i[1], 0)
		d[i[1]] += 1
		napis += [i[1]]
	elif i[0] == "ZMIEN":
		napis[-1] = i[1]
	elif i[0] == "USUN":
		napis = napis[:-1]
	elif i[0] == "PRZESUN":
		if i[1] in napis:
			tmp = napis.index(i[1])
			napis[tmp] = chr((ord(i[1]) + 1)) if i[1] != 'Z' else 'A'

print(f"4.1: {len(napis)}")
print(f"\n4.2: rodzaj: {mrodzaj}; długość: {mdl}")
litera4_3 = max(d, key=lambda x: d[x])
print(f"\n4.3: litera {litera4_3} {d[litera4_3]} razy" )
print("\n4.4")
print(''.join(napis))
