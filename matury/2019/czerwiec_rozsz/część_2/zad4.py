#!/usr/bin/env python3
liczby = []
pierwsze = []
with open('MIN-R2A1P-193_dane/liczby.txt','r') as f:
	for i in f:
		liczby.append(int(i.strip()))
with open('MIN-R2A1P-193_dane/pierwsze.txt','r') as f:
	for i in f:
		pierwsze.append(int(i.strip()))

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

# 4.1
ile1 = 0
with open('wyniki4_1.txt','w') as f:
	for i in liczby:
		if 100 <= i <= 5000 and is_prime(i):
			ile1 += 1
			f.write(f"{i}\n")
print(f"4.1: {ile1}")

# 4.2
ile2 = 0
with open('wyniki4_2.txt','w') as f:
	for i in pierwsze:
		if is_prime(i) and is_prime(int(str(i)[::-1])):
			ile2 += 1
			f.write(f"{i}\n")
print(f"4.2: {ile2}")

# 4.3
ile3 = 0
for i in pierwsze:
	while i > 9:
		i = sum(map(int, str(i)))
	if i == 1:
		ile3 += 1
print(f"4.3: {ile3}")
