#!/usr/bin/env python3

dane = []
with open('Dane_PR/liczby.txt','r') as f:
	for i in f:
		dane.append(int(i))

# 4.1
ile1 = 0
for i in dane:
	z = 0
	while i > 0:
		z +=  i % 3
		i = (i // 3)

	if z == 1:
		ile1 += 1

print(f"4.1: {ile1}")

# 4.2
def silnia(x):
	if x in (0,1):
		return 1 
	return x * silnia(x-1)

ile2 = 0
zad2 = []
for i in dane:
	s = sum(silnia(int(y)) for y in str(i))
	if i == s:
		ile2 += 1
		zad2.append(i)

print(f"4.2: {ile2=}: {zad2}")

# 4.3

def nwd(a,b):
	while b != 0:
		a,b = b, a % b
	return a

n = dane[0]
pocz = dane[0]
l = 1
m_l = 0
m_n = 0
m_pocz = 0
last = 0
for i in dane[1:]:
	if nwd(i,n) != 1:
		l += 1
		n = nwd(i,n)
	else:
		if l > m_l:
			m_l = l
			m_pocz = pocz
			m_n = n

		if nwd(last,i) != 1:
			pocz = last
			l = 2	

		else:
			pocz = i
			l = 1
		n = i
	last = i

print(f"4.3: długość: {m_l}; początek: {m_pocz}; dzielnik: {m_n}")

