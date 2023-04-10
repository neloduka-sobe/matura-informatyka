#!/usr/bin/env python3

def f(a,b,c):
	return ((c[1]-a[1])*(b[0]-a[0]) - (c[0]-a[0])*(b[1]-a[1])) == 0

def przynaleznosc(a,b,c):
	return c[0] >= min(a[0], b[0]) and c[0] <= max(a[0], b[0]) and c[1] >= min(a[1], b[1]) and c[1] <= max(a[1],b[1]) and f(a,b,c)


if __name__ == "__main__":
	print(f([-2,0],[7,3], [4,2]))
	print(przynaleznosc([-2,0],[7,3], [4,2]))
