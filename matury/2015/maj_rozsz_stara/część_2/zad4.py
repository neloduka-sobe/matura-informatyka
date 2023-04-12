#!/usr/bin/env python3

dane = []

with open('Dane/slowa.txt','r') as f:
	for i in f:
		dane.append(i.strip())

# 4.1
ile1 = 0
for i in dane:
	ile1 += i.count('0') > i.count('1')

print(f"4.1: {ile1}")

# 4.2
ile2 = 0
for i in dane:
	z = i.count('10') + i.count('01')
	if z == 1 and i[0] == '0':
		ile2 += 1

print(f"4.2: {ile2}")

# 4.3
ml = 0
m = []
last = 0
for i in dane:
	l = 0
	for y in i:
		if y == '0':
			l += 1
			if l > ml:
				ml = l
				m = []
		else:
			if l == ml:
				m.append(i)
			l = 0

	if l == ml:
		m.append(i)
	last = i				

print("4.3")
print("Długość:", ml)
print("Wystąpienia:", m)
