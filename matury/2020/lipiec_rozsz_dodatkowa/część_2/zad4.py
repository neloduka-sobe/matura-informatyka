#!/usr/bin/env python3

dane = []
with open('DANE/identyfikator.txt','r') as f:
	for i in f:
		dane.append(i.strip())

d = {}
zad4_2 = []
wagi = [7,3,1,7,3,1,7,3]
niepop = []
for i in dane:
	# 4.1
	s = sum(int(y) for y in i[3:])
	d.setdefault(s, [])
	d[s] = d[s] + [i]

	# 4.2
	if i[:3] == i[:3][::-1] or i[3:] == i[3:][::-1]:
		zad4_2.append(i)

	# 4.3
	# ord(z) - 55
	k = 0
	for ind,y in enumerate(i[:3] + i[4:]):
		if y.isalpha():
			k += (ord(y) - 55)*wagi[ind]
		else:
			k += int(y)*wagi[ind]
	if int(i[3]) != k%10:
		niepop.append(i)
	
	

m = max(d)
print(f"4.1: max: {m} dla {d[m]}")
print(f"4.2: {zad4_2}")
print(f"4.3: {niepop}")
