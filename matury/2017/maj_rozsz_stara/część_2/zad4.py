#!/usr/bin/env python3

dane = []
with open('Dane_PR/binarne.txt','r') as f:
	for i in f:
		dane.append(i.strip())


# 4.1
a = []
ile1 = 0
for i in dane:
	mid = len(i) //2
	if i[:mid] == i[mid:]:
		ile1 += 1
		a.append(i)

print("4.1")
print("Ilość:",ile1)
odp1 = max(a,key=len)
print("Napis:",odp1)
print("Długość:",len(odp1))

# 4.2
ile2 = 0
m_l = float('inf')
for i in dane:
	i = '0'*(len(i)%4) + i
	teza = True
	for y in range(len(i), 3, -4):
		if int(i[y-4:y],2) > 9:
			teza = False
			if len(i) < m_l:
				m_l = len(i)
			break
	ile2 += not teza

print("\n4.2")
print("Ilość:",ile2)
print("Długość najkrótszego:",m_l)

# 4.3
odp3 = max(dane, key=lambda x: int(x,2) if int(x,2) <= 65535 else 0)
print("\n4.3")
print(f"Para: {odp3}, {int(odp3,2)}")
