#!/usr/bin/env python3

dane = []

with open("DANE/liczby.txt","r") as f:
	for i in f:
		dane.append(int(i.strip()))

def is_prime(x):
	if x < 2:
		return False
	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

# 4.1
print("Zad. 4.1")
print("Wszystkie odbicia")
for i in dane:
	print(str(i)[::-1])

print("\nOdbicia podzielne przez 17")
for i in dane:
	if int(str(i)[::-1]) % 17 == 0:
		print(str(i)[::-1])

# 4.2
print("\nZad. 4.2")
m = 0
m_l = 0
for i in dane:
	a = abs(i - int(str(i)[::-1]))
	if a > m:
		m = a
		m_l = i

print(f"Maks: {m}; dla {m_l}")

# 4.3
print("\nZad. 4.3")
for i in dane:
	if is_prime(i) and is_prime(int(str(i)[::-1])):
		print(i)

# 4.4
print("\nZad. 4.4")
print('a):', len(set(dane)))

d = {}
for i in dane:
	d.setdefault(i, 0)
	d[i] += 1

b = 0
for i in d.keys():
	if d[i] == 2:
		b += 1
print(f"b): {b}")

c = 0
for i in d.keys():
	if d[i] == 3:
		c += 1
print(f"c): {c}")
