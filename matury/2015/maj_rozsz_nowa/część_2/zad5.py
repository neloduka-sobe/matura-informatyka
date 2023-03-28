#!/usr/bin/env python3

dane = []

with open("Dane_PR/kraina.txt", 'r') as f:
	for i in f:
		dane.append(i.strip().split(';'))

# 5.1
d = {}
for i in dane:
	region = i[0][-1]
	d.setdefault(region, 0)
	d[region] += int(i[1]) + int(i[2])

with open("wykres5.csv","w") as f:
	f.write("Region,ludność\n")
	for x,y in d.items():
		f.write(f"{x},{y}\n")

# 5.2
d2 = {}
for i in dane:
	region = i[0][-1]
	d2.setdefault(region, 0)
	if int(i[1])<int(i[3]) and int(i[2])<int(i[4]):
		d2[region] += 1

print("5.2")
for x,y in d2.items():
	print(f"Region: {x} ilość: {y}")	

# 5.3
d3 = {}
suma = 0
przeludnienie = 0
p = False
for i in dane:

	i[1:] = map(int,i[1:])
	mieszkancy = sum(i[3:])
	pocz = i[1]+i[2]
	t_w = mieszkancy / pocz
	t_w = int(t_w*10000) / 10000
	woj = i[0]
	y = 2015

	while mieszkancy / pocz <= 2 and y <= 2025:
		mieszkancy = mieszkancy * t_w		
		mieszkancy = int(mieszkancy)
		y += 1

	d3[woj] = mieszkancy
	suma += mieszkancy
	if mieszkancy / pocz > 2:
		przeludnienie += 1

print("\n5.3")
print(f"{suma=}")
print(f"{przeludnienie=}")
print(f"Najwięcej mieszkańców: {max(d3,key=lambda x: d3[x])}")
