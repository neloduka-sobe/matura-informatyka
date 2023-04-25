#!/usr/bin/env python3
kod_kreskowy = {}
with open('MIN-R2A1P-153_dane/cyfra_kodkreskowy.txt','r') as f:
	for ind,i in enumerate(f):
		if ind != 0:
			tmp = i.strip().split()
			kod_kreskowy[tmp[0]] = tmp[1]

kody = []
with open('MIN-R2A1P-153_dane/kody.txt','r') as f:
	for i in f:
		kody.append(i.strip())


# 6.1
with open('kody1.txt','w') as f:
	for i in kody:
		s1 = sum(int(y) for y in i[::2])
		s2 = sum(int(y) for y in i[1::2])
		f.write(f"{s1} {s2}\n")

# 6.2
with open('kody2.txt','w') as f:
	for i in kody:
		s1 = sum(int(y) for y in i[::2])
		s2 = sum(int(y) for y in i[1::2])
		kontr = (s1*3 + s2) % 10
		kontr = (10 - kontr) % 10
		kontr = kod_kreskowy[str(kontr)]
		f.write(f"{kontr}\n")

# 6.3
start = '11011010'
stop = '11010110'
with open('kody3.txt','w') as f:
	for i in kody:
		ret = start
		for y in i:
			ret += kod_kreskowy[y]
		s1 = sum(int(y) for y in i[::2])
		s2 = sum(int(y) for y in i[1::2])
		kontr = (s1*3 + s2) % 10
		kontr = (10 - kontr) % 10
		kontr = kod_kreskowy[str(kontr)]
		ret += kontr
		ret += stop
		f.write(f"{ret}\n")
	
