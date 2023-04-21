#!/usr/bin/env python3

dane = []
with open('MIN-DANE-2017/punkty.txt','r') as f:
	for i in f:
		dane.append(list(map(int,i.strip().split())))

def is_prime(x):
	if x < 2:
		return False
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

# 4.1
ile1 = 0
for i in dane:
	if is_prime(i[0]) and is_prime(i[1]):
		ile1 += 1

print(f"4.1: {ile1}")

# 4.2
ile2 = 0
for i in dane:
	if set(str(i[0])) == set(str(i[1])):
		ile2 += 1

print(f"\n4.2: {ile2}")

# 4.3
m = 0
mp = []
for ind,i in enumerate(dane):
	for y in dane[ind+1:]:
		tmp = ((i[0]-y[0])**2+(y[1]-i[1])**2)**0.5
		if tmp > m:
			m = tmp
			mp = [i,y]
print(f"\n4.3: max: {round(m)} dla {mp}")

# 4.4
a4 = 0
b4 = 0
c4 = 0
for i in dane:
	x,y = i
	if x in (5000, -5000) and -5000 < y < 5000:
		b4 += 1
	elif y in (5000, -5000) and -5000 < x < 5000:
		b4 += 1

	elif -5000 < x < 5000 and -5000 < y < 5000:
		a4 += 1
	else:
		c4 += 1
print(f"\n4.4: {a4},{b4},{c4}")
	
