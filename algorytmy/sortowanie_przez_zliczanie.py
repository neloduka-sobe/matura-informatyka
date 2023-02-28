#!/usr/bin/env python3
import random
from time import sleep

def counting_sort_1(arr):
	b = dict()
	for i in arr:
		if i in b.keys():
			b[i] += 1
		else:
			b[i] = 1

	ret = []
	for i in range(max(b.keys())+1):
		if i in b.keys():
			ret += [i]*b[i]
	return ret

def counting_sort_2(arr):
	b = [0 for i in range(max(arr)+1)]
	for i in arr:
		b[i] += 1
	ret = []
	for i in range(len(b)):
		ret += [i]*b[i]
	return ret

def counting_sort_3(arr):
	b = [0 for i in range(max(arr)+1)]
	for i in arr:
		b[i] += 1

	for i in range(1, len(b)):
		b[i] += b[i-1]

	c = [0 for i in range(b[-1]+1)]
	for i in arr:
		c[b[i]] = i
		b[i] -= 1
	return c[1:]

if __name__ == "__main__":
    for i in range(100):
        a = []
        for i in range(10):
            a.append(random.choice(range(100)))
        print('######')
        print(counting_sort_1(a) == sorted(a))
        print(counting_sort_2(a) == sorted(a))
        print(counting_sort_3(a) == sorted(a))
        sleep(1)
