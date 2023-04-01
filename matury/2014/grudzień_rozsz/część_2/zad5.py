#!/usr/bin/env python3

dane = []

with open('DANE_PR/dziennik.txt','r') as f:
	for i in f:
		dane.append(int(i.strip()))

ilosc_1 = 0
m = 0
mp = ''
mk = ''
p = ''
k = ''
l = 0
last = 0
for i in dane:
	if last < i:
		l += 1
	else:
		k = last
		if l > m:
			m = l
			mp = p
			mk = k
		if l > 3:
			ilosc_1 += 1
		p = i
		l = 1
	last = i
			

print(f"5.1: {ilosc_1}")
print(f"5.2 max: {max(dane)} w {dane.index(max(dane))+1} dniu")
print(f"5.2 min: {min(dane)} w {dane.index(min(dane))+1} dniu")
print(f"5.3: dlugosc: {m}; różnica: {mk-mp} cm")
