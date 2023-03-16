#!/usr/bin/env python3
from math import ceil

def f(x):
	return x**2 + x + 1

def calka_pros(a, b, krok, funkcja):
	'''Wyznaczanie pola pod wykresem metodą prostokątów'''
	s = 0
	i = ceil(10/krok)
	for y in range(a*i, b*i+1, int(krok*i)):
		s += krok*f(y/i)
	return s


def calka_trap(a, b, krok, funkcja):
	'''Wyznaczanie pola pod wykresem metodą trapezów'''
	s = 0
	i = ceil(10/krok)
	l = f(a)
	for y in range(a*i, b*i+1, int(krok*i)):
		s += ((l + f(y/i))*krok)/2
		l = f(y/i)
	return s

if __name__ == "__main__":
	print(calka_pros(1,10,0.0001, f))
	print(calka_trap(1,10,0.0001, f))
