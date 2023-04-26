#!/usr/bin/env python3
import random
from time import sleep

def quick(arr):
	if len(arr) in (0,1):
		return arr
	piv = len(arr) // 2
	l = []	
	r = []
	for ind,i in enumerate(arr):
		if ind == piv:
			continue
		elif i < arr[piv]:
			l.append(i)
		else:
			r.append(i)
	return quick(l) + [arr[piv]] + quick(r)

def quick2(arr,left,right):
	if left >= right:
		return

	piv = arr[left]
	l = left + 1
	r = right
	while l <= r:
		while l <= r and arr[r] >= piv:
			r -= 1
		while l <= r and arr[l] <= piv:
			l += 1
		if l <= r:
			arr[l], arr[r] = arr[r], arr[l]
	print(arr)
	arr[left], arr[r] = arr[r], arr[left]
	print(arr)
	quick2(arr, left, r-1)
	quick2(arr, r+1, right)

if __name__ == "__main__":
    for i in range(100):
        a = []
        for i in range(10):
            a.append(random.choice(range(100)))
        b = a
        print('######')
        print(quick(a)==sorted(a))
        quick2(a,0, len(a)-1)
        print(a == sorted(b))
        sleep(0.1)
