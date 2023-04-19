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

# 1.3
ile3 = {}
ile3.setdefault('w',0)
ile3.setdefault('W',0)
for i in dane:
	lok = {}
	for indy, y in enumerate(i):
		for indx,x in enumerate(y):
			if x != '.':
				lok.setdefault(x, [])
				lok[x] += [[indx,indy]]

	for w,k in zip(['w', 'W'],['K','k']):
		t = []
		if w in lok.keys():
			krol = lok[k][0]
			for wieza in lok[w]:
				teza = True
				if wieza[0] == krol[0]:
					for z in 'shgpSHGP' + ('W' if w.islower() else 'w'):
						if z in lok.keys():
							for y in lok[z]:
								if y[0] == wieza[0] and (min(wieza[1], krol[1]) < y[1] < max(wieza[1], krol[1])):
									teza = False
									break
				elif wieza[1] == krol[1]:
					for z in 'shgpSHGP' + ('W' if w.islower() else 'w'):
						if z in lok.keys():
							for y in lok[z]:
								if y[1] == wieza[1] and (min(wieza[0], krol[0]) < y[0] < max(wieza[0], krol[0])):
									teza = False
									break
				else:
					teza = False
				if teza:
					t.append(True)
		else:
			t.append(False)

		if any(t):
			ile3[w] += 1

print(f"\n1.3\n{ile3['W']}; {ile3['w']}")
