#!/usr/bin/env python3

dane = []

with open('MIN-R2A1P-163_dane/liczby.txt','r') as f:
	for i in f:
		dane.append(i.strip())

# 6.1
ile_1 = 0
for i in dane:
	if i[-1] == '8':
		ile_1 += 1
print(f"6.1: {ile_1}")

# 6.2
ile_2 = 0
for i in dane:
	if i[-1] == "4" and '0' not in i:
		ile_2 += 1
print(f"6.2: {ile_2}")

# 6.3
ile_3 = 0
for i in dane:
	if i[-1] == '2' and i[-2] == '0':
		ile_3 += 1
print(f"6.3: {ile_3}")

# 6.4
suma = 0
for i in dane:
	if i[-1] == '8':
		suma += int(i[:-1], 8)
print(f"6.4: {suma}")

# 6.5
nm = ''
nw = ''
nm_w = float('inf')
nw_w = 0
for i in dane:
	y = int(i[:-1], int(i[-1]))
	if y > nw_w:
		nw = i
		nw_w = y
	if y < nm_w:
		nm = i
		nm_w = y
print(f"Największa kod: {nw} wartość dzies.: {nw_w}")
print(f"Najmniejsza kod: {nm} wartość dzies.: {nm_w}")
