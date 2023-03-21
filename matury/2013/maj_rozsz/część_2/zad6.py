#!/usr/bin/env python3

dane = []

with open('Dane/dane.txt', 'r') as f:
	for i in f:
		dane.append(int(i.strip()))

ile_a = 0
ile_b = 0
ile_c = 0
najm_c = float('inf')
najw_c = 0
for i in dane:
	i = str(i)
	
	# a)
	a = str(i)
	if a[0] == a[-1]:
		ile_a += 1

	# b)
	b = str(int(i, 8))
	if b[0] == b[-1]:
		ile_b += 1

	y = 1
	teza = True
	while y < len(i):
		if i[y-1] > i[y]:
			teza = False
			break
		y += 1	

	if teza:
		tmp = int(i,8)
		if tmp > najw_c:
			najw_c = tmp
		if tmp < najm_c:
			najm_c = tmp	
		ile_c += 1

print(f"a) {ile_a}")
print(f"b) {ile_b}")
print(f"c) liczba: {ile_c}; najmniejsza: {oct(najm_c)[2:]}; największa: {oct(najw_c)[2:]}")
