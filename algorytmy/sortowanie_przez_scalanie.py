#!/usr/bin/env python3
import random

def merge_sort_1(arr):
	if len(arr) == 1:
		return arr

	mid = len(arr) // 2
	l = merge_sort_1(arr[:mid])
	r = merge_sort_1(arr[mid:])
	ret = []
	while len(r) != 0 or len(l) != 0:
		if len(r) == 0:
			ret.append(l.pop(0))
		elif len(l) == 0:
			ret.append(r.pop(0))
		elif r[0] >= l[0]:
			ret.append(l.pop(0))
		else:
			ret.append(r.pop(0))
	return ret

 
if __name__ == "__main__":
		for i in range(100):
			arr = [random.randint(1,100) for i in range(10)]
			print(merge_sort_1(arr) == sorted(arr))
