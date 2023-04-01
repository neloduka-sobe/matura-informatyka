#!/usr/bin/env python3

dane = []
with open("dane/dane.txt",'r') as f:
	for i in f:
		t = [int(y) for y in i.strip().split()]
		dane.append(t)

# a)

# 1.
a1 = 0
b1 = 0
c1 = 0
d1 = 0
e1 = 0
f1 = 0
for i in dane:
	a1 += i[0]
	b1 += i[1]
	c1 += i[2]
	d1 += i[3]
	e1 += i[4]
	f1 += i[5]

print(f"a) 1.: {a1=} {b1=} {c1=} {d1=} {e1=} {f1=}")

# 2.
ma = ''
ma_w = 0
mi = ''
mi_w = float('inf')
for ind,i in enumerate(dane):
	if sum(i) > ma_w:
		ma = ind+1
		ma_w = sum(i)
	elif sum(i) < mi_w:
		mi = ind+1
		mi_w = sum(i)

print(f"a) 2.: Min: {mi_w} dla {mi}; Max: {ma_w} dla {ma}")

# 3. i 4.
mad = {a: 0 for a in ['A','B','C','D','E','F']}
for ind,i in enumerate(dane):
	mandaty = i[-1]
	i = i[:-1]
	
	okr = {a: 0 for a in ['A','B','C','D','E','F']}
	while mandaty > 0:
		tmp = {a: b/(okr[a]+1) for a,b in zip(['A','B','C','D','E','F'],i)}
		m = max(tmp, key=lambda x: tmp[x])
		okr[m] += 1
		mandaty -= 1


	for key in okr.keys():
		mad[key] += okr[key]
	# 3.
	if ind == 5:
		for key in okr.keys():
			print(f"Komitet: {key} ilość: {okr[key]}")

# 4.
print("a) 4.")
for key in mad.keys():
	print(f"Komitet: {key} ilość: {mad[key]}")

# b)
with open('wykres.csv', 'w') as f:
	f.write(f"Komitet, Ilość głosów\n")
	for key in mad.keys():
		f.write(f"{key},{mad[key]}\n")
