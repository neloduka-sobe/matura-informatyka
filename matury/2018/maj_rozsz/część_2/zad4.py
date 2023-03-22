#!/usr/bin/env python3

dane = []

with open("Dane_PR/sygnaly.txt", 'r') as f:
	for i in f:
		dane.append(i.strip())

# 4.1
print("Zad. 4.1")
for i in range(39,len(dane), 40):
	print(dane[i][9], end='')
print()

# 4.2 
d = {}
for i in dane:
	u = len(set(i))
	d[i] = u

print("Zad. 4.2")
m = max(d, key=lambda x: d[x])
print(f"ilość: {d[m]} dla {m}")

# 4.3
print("Zad. 4.3")
for i in dane:
	teza = True
	for y in i:
		for z in i:
			if abs(ord(y)-ord(z)) > 10:
				teza = False
				break
		if not teza:
			break
	if teza:
		print(i)
