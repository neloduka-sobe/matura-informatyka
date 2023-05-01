#!/usr/bin/env python3
dane = []

with open('Dane_PR/dane.txt','r') as f:
	for i in f:
		i = list(map(int, i.strip().split()))
		dane.append(i)

# 6.1
ma = 0
mi = float('inf')
for i in dane:
	for y in i:
		if y > ma:
			ma = y
		if y < mi:
			mi = y
print(f"6.1: Najjaśniejszy: {ma}; Najciemniejszy: {mi}")

# 6.2
ile2 = 0
for i in dane:
	for y in range(len(i)//2+1):
		if i[y] != i[-1-y]:
			ile2 += 1
			break
print(f"6.2: {ile2}")

# 6.3
ile3 = 0
for y in range(len(dane)):
	for x in range(len(dane[y])):
		if (x-1) >= 0 and abs(dane[y][x-1] - dane[y][x]) > 128:
			ile3 += 1
		elif (x+1) < len(dane[y]) and abs(dane[y][x+1] - dane[y][x]) > 128:
			ile3 += 1
		elif (y-1) >= 0 and abs(dane[y-1][x] - dane[y][x]) > 128:
			ile3 += 1
		elif (y+1) < len(dane) and abs(dane[y+1][x] - dane[y][x]) > 128:
			ile3 += 1
	
print(f"6.3: {ile3}")

# 6.4
m_dl = 0
dl = 0
for x in range(len(dane[y])):
	for y in range(1,len(dane)):
		if dane[y][x] == dane[y-1][x]:
			dl += 1
		else:
			if dl > m_dl:
				m_dl = dl
			dl = 1
print(f"6.4: {m_dl}")

