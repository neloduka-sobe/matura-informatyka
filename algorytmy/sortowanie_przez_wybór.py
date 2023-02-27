#!/usr/bin/env python3
import random
from time import sleep

def selection_sort(arr):
	for i in range(len(arr)):
		m = i
		for y in range(i+1, len(arr)):
			if arr[y] < arr[m]:
				m = y
		arr[m],arr[i] = arr[i], arr[m]
	return arr

if __name__ == "__main__":
    for i in range(100):
        a = []
        for i in range(10):
            a.append(random.choice(range(100)))
        print('######')
        print(selection_sort(a) == sorted(a))
        sleep(1)
	
	
