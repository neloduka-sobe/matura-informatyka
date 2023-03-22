#!/usr/bin/env python3

def is_prime(x):
	if x < 2:
		return False
	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

def super_prime(x):
	return is_prime(x) and is_prime(sum(int(i) for i in str(x)))


def super_b_prime(x):
	return super_prime(x) and is_prime(bin(x)[2:].count('1'))

print("Zadanie 5.")
print("a)")
ile_b = 0
suma_b = 0
# a)
with open('1.txt', 'w') as f:
	print("<2,1000>")
	p_1 = 0
	for i in range(2, 1001):
		if super_b_prime(i):
			p_1 += 1
			f.write(str(i)+'\n')
	print(p_1)

with open('2.txt', 'w') as f:
	print("<100,10000>")
	p_2 = 0
	for i in range(100, 10001):
		if super_b_prime(i):
			p_2 += 1
			f.write(str(i)+'\n')
		if is_prime(sum(int(y) for y in str(i))):
			ile_b +=1
			suma_b += i
	print(p_2)

with open('3.txt', 'w') as f:
	print("<1000,100000>")
	p_3 = 0
	for i in range(1000, 100001):
		if super_b_prime(i):
			p_3 += 1
			f.write(str(i)+'\n')
	print(p_3)

# b)
print(f"\nb) {ile_b}")
print(is_prime(suma_b))
