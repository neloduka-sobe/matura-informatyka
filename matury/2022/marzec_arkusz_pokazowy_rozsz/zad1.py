#!/usr/bin/env python3

dane = []

with open('Dane/szachy.txt','r') as f:
	p = []
	for i in f:
		if i.strip() == '':
			dane.append(p)	
			p = []
			continue
		p.append(i.strip())

# 1.1

ile1 = 0
m1 = 0
for i in dane:
	k = [0 for i in range(8)]
	m = 0
	for y in i:
		for ind,z in enumerate(y):
			if z != '.':
				k[ind] += 1
	m = k.count(0)
	if m > 0:
		ile1 += 1

	if m > m1:
		m1 = m

print(f"1.1\n{ile1}; {m1}")

# 1.2
najm2 = float('inf')
ile2 = 0
for i in dane:
	b1 = {}
	b2 = {}
	n = 0
	for y in i:
		for ind,z in enumerate(y):
			if z != '.':
				if z.islower():
					b1.setdefault(z,0)
					b1[z] += 1
				else:
					z = z.lower()
					b2.setdefault(z,0)
					b2[z] += 1
	if b1 == b2:
		ile2 += 1

		n = sum(b2.values())*2
		if n < najm2:
			najm2 = n

print(f"\n1.2\n{ile2}; {najm2}")
