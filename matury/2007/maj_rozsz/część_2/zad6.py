#!/usr/bin/env python3

dane = []

with open('Dane/telefony.txt', 'r') as f:
	for i in f:
		dane.append(i.strip())


print("Zadanie 6")
# a)
print(f"a) {dane.count('504669045')}\n")

# b)
b = {}
for i in dane:
	b.setdefault(i, 0)
	b[i] += 1
k = sorted(b.keys(), key=lambda x: b[x])[-1]
print(f"b) {b[k]} razy dla numeru {k}\n")

# c)
ile_c = 0
for i in dane:
	if i.startswith("511"):
		ile_c += 1
print(f"c) {ile_c}\n")

# d)
ile_d = 0
for i in dane:
	suma = 0
	for y in i:
		y = int(y)
		if y % 2 == 0:
			suma += y
	if suma > 42:
		ile_d += 1

print(f"d) {ile_d}\n")

# e)
ile_e = 0
for i in dane:
	if i.count('1') >= 4:
		ile_e += 1

print(f"e) {ile_e}\n")

# f)
ile_f = 0
for i in dane:
	if i[-1] == '2' and int(sorted(i)[4]) % 3 == 0:
		ile_f += 1

print(f"f) {ile_f}\n")

# g)
print("g)")
for i in sorted(b.keys(), key=lambda x: b[x], reverse=True):
	if b[i] >= 2:
		print(i, b[i],sep='\t')


