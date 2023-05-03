#!/usr/bin/env python3
dane_6_1 = []
dane_6_2 = []
dane_6_3 = []

with open('Dane_NOWA/dane_6_1.txt','r') as f:
	for i in f:
		dane_6_1.append(i.strip())

with open('Dane_NOWA/dane_6_2.txt','r') as f:
	for i in f:
		i = i.strip().split()
		if len(i) == 2:
			i[1] = int(i[1])
		dane_6_2.append(i)

with open('Dane_NOWA/dane_6_3.txt','r') as f:
	for i in f:
		i = i.strip().split()
		dane_6_3.append(i)

def szyfr(text, k):
	k %= 26
	ret = ''
	for i in text:
		c = ord(i)+k
		if c > 90:
			c -= 26
		ret += chr(c)
	return ret

def deszyfr(text, k):
	k %= 26
	ret = ''
	for i in text:
		c = ord(i)-k
		if c < 65:
			c += 26
		ret += chr(c)
	return ret

# 6.1
with open('wyniki_6_1.txt','w') as f:
	for i in dane_6_1:
		f.write(f"{szyfr(i,107)}\n")
print('6.1 w pliku wyniki_6_1.txt')

# 6.2
with open('wyniki_6_2.txt','w') as f:
	for i in dane_6_2:
		if len(i) != 2:
			continue
		f.write(f"{deszyfr(i[0],i[1])}\n")
print('6.2 w pliku wyniki_6_2.txt')

# 6.3
with open('wyniki_6_3.txt','w') as f:
	for i in dane_6_3:
		r = abs(ord(i[0][0]) - ord(i[1][0])) % 26
		l = 1
		for x in range(1,len(i[0])):
			tmp = (abs(ord(i[1][x]) - ord(i[0][x])) % 26)
			if r == tmp or r == 26-tmp:
				l += 1

		if l != len(i[0]):
			f.write(f"{i[0]}\n")
			
print('6.3 w pliku wyniki_6_3.txt')
