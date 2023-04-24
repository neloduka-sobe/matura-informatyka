#!/usr/bin/env python3

dane = []
with open('Dane_2103/galerie.txt','r') as f:
	for i in f:
		i = i.strip().split()
		tmp = []
		tmp += i[:2]
		tmp += list(map(int,i[2:]))
		dane.append(tmp)

# 4.1
d1 = {}
for i in dane:
	d1.setdefault(i[0],0)
	d1[i[0]] += 1

print("4.1")
for i in d1.keys():
	print(f"{i}: {d1[i]}")

# 4.2
print("4.2 a)\n w pliku wynik4_2a.txt")
n = float('inf')
nn = ''
m = 0
mn = ''
with open('wynik4_2a.txt','w') as f:
	for i in dane:
		s = sum(i[y]*i[y-1] for y in range(3,len(i),2))
		ile = sum(1 for y in range(3, len(i),2) if i[y]!=0 and i[y-1]!=0)
		if s > m:
			m = s
			mn = i[1]
		if s < n:
			n = s
			nn = i[1]
		f.write(f"{i[1]}: {s}; {ile}\n")

print("4.2 b)")
print(f"Max: {m} dla {mn}")
print(f"Min: {n} dla {nn}")

# 4.3
m3 = 0
mn3 = ''
n3 = float('inf')
nn3 = ''
for i in dane:
	s = set(int(i[y]*i[y-1]) for y in range(3,len(i),2))
	l = len(s)
	if 0 in s:
		l -= 1
	if l > m3:
		m3 = l
		mn3 = i[1]
	if l < n3:
		n3 = l
		nn3 = i[1]		
		

	
print("4.3")
print(f"Max: {m3} dla {mn3}")
print(f"Min: {n3} dla {nn3}")
