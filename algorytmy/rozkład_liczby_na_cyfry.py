#!/usr/bin/env python3

def rozklad_1(x):
	return [int(a) for a in str(x)]

def rozklad_2(x):
	ret = []
	while x > 0:
		ret.append(x%10)
		x //= 10
	return ret[::-1]

if __name__ == "__main__":
	print(rozklad_1(1000))
	print(rozklad_1(99999))
	print(rozklad_2(1000))
	print(rozklad_2(99999))
	print(rozklad_2(12542423))
