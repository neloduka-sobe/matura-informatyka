#!/usr/bin/env python3

dane = []

with open('Dane/przyklad.txt','r') as f:
	for i in f:
		dane.append(int(i.strip()))

# 4.1
ile_1 = 0
pierwsza = 0
for i in dane:
	i = str(i)
	if i[0] == i[-1]:
		if pierwsza == 0:
			pierwsza = int(i)
		ile_1 += 1

print("Zad. 4.1")
print(f"{ile_1=} {pierwsza=}")

def rozklad(x):
	cp = x
	ret = []
	i = 2
	while i <= int(cp**0.5)+1:
		while x % i == 0:
			ret += [i]
			x //=i
		i += 1
	if x > 1:
		ret += [x]
	return ret

# 4.2
print("4.2")
# a)
m_a = 0
i_a = 0
for i in dane:
	l = len(rozklad(i))
	if l > m_a:
		m_a = l
		i_a = i
print(f"a) {m_a} dla {i_a}")

# b)
m_b = 0
i_b = 0
for i in dane:
	l = len(set(rozklad(i)))
	if l > m_b:
		m_b = l
		i_b = i
print(f"b) {m_b} dla {i_b}")
