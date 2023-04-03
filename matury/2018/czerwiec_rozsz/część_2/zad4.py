#!/usr/bin/env python3

dane1 = []
with open('NM_DANE_PR/dane1.txt','r') as f:
	for i in f:
		dane1.append([int(y) for y in i.strip().split()])

dane2 = []
with open('NM_DANE_PR/dane2.txt','r') as f:
	for i in f:
		dane2.append([int(y) for y in i.strip().split()])

# 4.1
ile_1 = 0
for x,y in zip(dane1, dane2):
	if x[-1] == y[-1]:
		ile_1 += 1
print(f"4.1: {ile_1}")


# 4.2
ile_2 = 0
for x,y in zip(dane1, dane2):
	if sum(1 for i in x if i % 2) == 5 == sum(1 for i in y if i % 2)  == sum(1 for i in y if not i % 2) == sum(1 for i in x if not i % 2):
		ile_2 += 1
print(f"\n4.2: {ile_2}")

# 4.3
ile_3 = 0
nr_wierszy = []
for x,y in zip(dane1, dane2):
	if set(x) == set(y):
		ile_3 += 1
		nr_wierszy.append(dane1.index(x)+1)	
print(f"\n4.3: {ile_3}")
print(nr_wierszy)

# 4.4
print("\n4.4")
with open('wynik4_4.txt','w') as f:
	for x,y in zip(dane1, dane2):
		ret = []
		while len(x) > 0 or len(y) > 0:
			if len(x) == 0:
				ret.append(y.pop(0))
			elif len(y) == 0:
				ret.append(x.pop(0))
			elif y[0] > x[0]:
				ret.append(x.pop(0))
			else:
				ret.append(y.pop(0))
		print(*ret)
		f.write(' '.join(map(str,ret))+"\n")
