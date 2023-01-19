#!/usr/bin/env python3

dane = []
with open('Dane/liczby.txt') as f:
	for i in f:
		dane.append(int(i.strip()))

def is_prime(n):
	for i in range(2,int((n**0.5))+1):
		if n % i == 0:
			return False
	return True

def sito(n):
	ret=[True for i in range(n+1)]
	ret[0]=False
	ret[1]=False
	for i in range(2,n+1):
		if ret[i] == True:
			j = 2*i
		while j <= n:
			ret[j]=False
			j += i
	return ret

### 2.
ile2=0
for i in dane:
        # Można także stworzyć sito Erastotenesa do 100000 i sprawdzać, czy dana liczba jest w sicie
	if is_prime(i-1):
		ile2+=1
		
print("Zad 3.2", ile2)


### 3.
print("Zad 3.3")
maks = max(dane) # Albo = 1000000, gdyż taki jest przedział liczb
s = sito(maks)
najw = 0
najw_i = 0
najm = float('inf')
najm_i = 0

for i in dane:
    a = 2
    b = i - a
    l = 0
    while a <= b:
        if s[a] and s[b]:
            l += 1
        a += 1
        b -= 1
    if l > najw:
        najw = l
        najw_i = i
    elif l < najm:
        najm = l
        najm_i = i

print(f"{najw=} dla {najw_i=}")
print(f"{najm=} dla {najm_i=}")

### 4.
print('Zad 3.4')
s=''
for i in dane:
	s += hex(i)[2:]

for i in '0123456789abcdef':
	print(i.upper(), ':', s.count(i))
