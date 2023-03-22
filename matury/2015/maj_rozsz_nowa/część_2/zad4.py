#!/usr/bin/env python3
dane = []

with open('Dane_PR/liczby.txt', 'r') as f:
	for i in f:	
		dane.append(i.strip())

# 4.1
ile_1 = 0
for i in dane:
	if i.count('1') < i.count('0'):
		ile_1 += 1

print(f"Zad 4.1: {ile_1}")

# 4.2
p_2 = 0
p_8 = 0
for i in dane:
	if i.endswith('0'):
		p_2 += 1
	if i.endswith('000'):
		p_8 += 1
print(f"Zad 4.2 podzielne przez 2: {p_2}; podzielne przez 8: {p_8}")

# 4.3
mx = max(dane, key=lambda x: int(x,2))
mi = min(dane, key=lambda x: int(x,2))
print(f"Min: {mi}; nr wiersza: {dane.index(mi)+1}")
print(f"Max: {mx}; nr wiersza: {dane.index(mx)+1}")
