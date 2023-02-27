#!/usr/bin/env python3
import random
from time import sleep

def bubble_sort(arr):
    for i in range(len(arr)):
        for y in range(1, len(arr)-i):
            if arr[y-1] > arr[y]:
                arr[y-1],arr[y]=arr[y],arr[y-1]
    return arr

if __name__ == "__main__":
    for i in range(100):
        a = []
        for i in range(10):
            a.append(random.choice(range(100)))
        print('######')
        print(bubble_sort(a))
        sleep(1)



    
