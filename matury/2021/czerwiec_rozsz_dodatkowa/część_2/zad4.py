#!/usr/bin/env python3
dane = []
with open('DANE/napisy.txt','r') as f:
	for i in f:
		dane.append(i.strip())


# 4.1
ile_1 = 0
for i in dane:
	for y in i:
		if y.isdigit():
			ile_1 += 1
print(f"4.1: {ile_1=}")

# 4.2
haslo = ''
for i in range(20, len(dane)+1, 20):
	i -= 1
	haslo += dane[i][i//20]
print(f"\n4.2:{haslo=}")

# 4.3
ret = ''
for i in dane:
	if i[1:] == i[1:][::-1]: 
		ret += i[25]
	elif i[:-1] == i[:-1][::-1]:
		ret += i[24]
print(f"\n4.3: {ret}")

# 4.4
wynik_4 = ''
for i in dane:
	l = ''
	for y in i:
		if y.isdigit():
			l += y
		if len(l) == 2:
			if 65 <= int(l) <= 90:
				wynik_4 += chr(int(l))
			l = ''

	if wynik_4.endswith("XXX"):
		break

print(f"\n4.4:{wynik_4=}")
