#!/usr/bin/env python3

dane = []
with open("Dane/pesel.txt","r") as f:
	for i in f:
		dane.append(i.strip())

sa = 0
sb = 0
sc = {}
zle_pesele = []
e = {}
for i in dane:

	# a)
	if i[2:4] == '12':
		sa += 1
	
	# b)
	if int(i[-2]) % 2 != 1:
		sb += 1

	# c)
	rok = i[:2]
	sc.setdefault(rok, 0)
	sc[rok] += 1

	# d)
	wagi = [1,3,7,9,1,3,7,9,1,3]
	z = 0

	for tmp in range(10):
		z += (int(i[tmp]) * wagi[tmp])

	if (z % 10 != 10 - int(i[-1]) and z%10 != 0) or (0 == z%10 and z%10 !=  int(i[-1])):
		zle_pesele.append(i)

	# e)
	dekada = i[0]
	e.setdefault(dekada, 0)
	e[dekada] += 1
	


print(f"a): {sa}")
print(f"b): {sb}")
c = max(sc,key=lambda x: sc[x])
print(f"c): {sc[c]} dla roku 19{c}")
print("d)")
for i in sorted(zle_pesele):
	print(i)

# e)
with open('wykres.csv', 'w') as f:
	f.write("Dekada,Ilość\n")
	for i in e.keys():
		f.write(f"{i}0',{e[i]}\n")
