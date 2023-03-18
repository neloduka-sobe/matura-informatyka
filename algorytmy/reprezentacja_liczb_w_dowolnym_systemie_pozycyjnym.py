#!/usr/bin/env python3


def zamiana(liczba, system):
	y = 1
	z = 1
	ret = ''
	while z <= liczba:
		y += 1
		z *= system
	z //= system

	while z !=0:	
		ret += str(liczba // z)	
		liczba %= z
		z //= system
	return ret

def zamiana_2(liczba, system):
	ret = ''
	while liczba != 0:
		ret = str(liczba % system) + ret
		liczba //= system

	return ret

if __name__ == "__main__":
	for i in range(100):
		print(zamiana(i, 3))
		print(zamiana_2(i, 3))
		print("###")
