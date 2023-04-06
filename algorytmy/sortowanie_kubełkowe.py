#!/usr/bin/env python3
import random

def kubelkowe(arr, k):
	'''
	Link: https://www.youtube.com/watch?v=V0jC3ua7ZgI&list=PLpEP9TjZ__-Ff6YYZSZ0EAd54AdVFXOf5&index=26
	'''
	n = len(arr)
	kub = [[] for i in range(k)]
	for i in arr:
		kub[int(k*i)].append(i)
	ret = []
	for i in kub:
		ret += sorted(i)
	return ret

if __name__ == '__main__':
	k = 10
	arr = [0.1,0.2,0.3,0.05,0.4,0.5,0.6,0.7,0.8,0.9,0.099,0.21,0.54,0.5432,0.76,0.5]
	print(kubelkowe(arr[::-1],k))
		
