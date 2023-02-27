#!/usr/bin/env python3
import random
from time import sleep

def insertion_sort(arr):
    for i in range(1, len(arr)):
        y = i
        while y > 0:
            if a[y] < a[y-1]:
                a[y], a[y-1] = a[y-1], a[y]
                y -= 1
            else:
                break
    return arr

def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        y = i
        while y > 0 and a[y] < a[y-1]:
            a[y], a[y-1] = a[y-1], a[y]
            y -= 1
    return arr

if __name__ == "__main__":
    for i in range(100):
        a = []
        for i in range(10):
            a.append(random.choice(range(100)))
        print('######')
        print(insertion_sort(a) == sorted(a))
        print(insertion_sort_2(a) == sorted(a))
        sleep(1)
        
