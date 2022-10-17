#!/usr/bin/env python3

def hanoi(a,b,c,n):
    if n > 0:
        hanoi(a,c,b,n-1)
        print(a, "na", b)
        hanoi(c,b,a,n-1)
if __name__ == "__main__":
    hanoi('a', 'b', 'c', 3)
