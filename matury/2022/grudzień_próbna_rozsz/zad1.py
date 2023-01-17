#!/usr/bin/env python3
dane=''
with open('Dane/mecz.txt','r') as f:
	for i in f:
		dane=i.strip()	

#dane='BBBBBBBBBBAABBAAAAAAAAAAA'
### 1.
last = dane[0]
ile1=0
for i in dane:
	if i!= last:
		ile1+=1
	last = i
print("Zad 1.")
print(ile1)
#print(dane.count("AB")+dane.count("BA"))

### 2.
a=0
b=0
i=0
while not ((a >= 1000 or b >= 1000) and abs(a-b) >= 3):
	if dane[i] == "A":
		a += 1
	elif dane[i] == 'B':
		b+=1
	i+=1

print("Zad 2.")
print(f"A|{a}:{b}|B")

# Błąd z końcem, ale nie ma go w pliku
### 3.
ilosc=0
p = ''
dl=0
mdl=0
mdld=''
for ind,i in enumerate(dane):
	if p == '':
		p = i
		dl=1
	elif p == i:
		dl +=1
	elif p != i:
		if dl >= 10:
			ilosc+=1
			if dl > mdl:
				mdl=dl
				mdld=p
		p = i
		dl=1
print("Zad 3.")
print("Ilosc pass:",ilosc)
print(f"Najdluzsza: {mdl} dla druz:{mdld}")
