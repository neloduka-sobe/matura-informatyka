#!/usr/bin/env python3

dane = []

with open('dane_czII/dane_anagramy.txt','r') as f:
	for i in f:
		dane.append(i.strip().split())

ile1 = 0
d = {}
for i in dane:
	
	# a)
	if sorted(i[0]) == sorted(i[1]):
		ile1 += 1

	# b)
	d.setdefault(''.join(sorted(i[0])),0)
	d[''.join(sorted(i[0]))] += 1
	d.setdefault(''.join(sorted(i[1])),0)
	d[''.join(sorted(i[1]))] += 1

print("Zadanie 4.")
print("a)")
print(ile1)
print("b)")
print(max(d.values()))
