#!/usr/bin/env python3

dane = []

with open('dane_PR/NAPIS.TXT','r') as f:
	for i in f:
		dane.append(i.strip())

def is_prime(x):
	if x == 2:
		return True

	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

print("Zadanie 5.")
# a)
ile_a = 0
for i in dane:
	suma = sum(ord(y) for y in i)	
	if is_prime(suma):
		ile_a += 1

print(f"a) {ile_a}")

# b)
print("\nb)")
ile_b = 0
for i in dane:
	y = 1
	teza = True
	while y < len(i):
		if i[y-1] >= i[y]:
			teza = False
			break
		y += 1

	if teza:
		ile_b += 1
		print(i)

print(f"\nilość {ile_b}")

# c)
d = {}
for i in dane:
	d.setdefault(i, 0)
	d[i] += 1

print("\nc)")
print("napis\tilość")
for i in d.keys():
	if d[i] > 1:
		print(f"{i}\t{d[i]}")
