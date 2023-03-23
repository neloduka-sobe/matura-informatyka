#!/usr/bin/env python3

dane = []

with open('Dane/przyklad.txt','r') as f:
	for i in f:
		dane.append(int(i.strip()))

# 4.1
ile_1 = 0
pierwsza = 0
for i in dane:
	i = str(i)
	if i[0] == i[-1]:
		if pierwsza == 0:
			pierwsza = int(i)
		ile_1 += 1

print("Zad. 4.1")
print(f"{ile_1=} {pierwsza=}")
