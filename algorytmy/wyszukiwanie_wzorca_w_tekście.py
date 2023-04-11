#!/usr/bin/env python3

def wzorzec(t,wz):
	for i in range(len(t)-len(wz)):
		k = True
		for j in range(len(wz)):
			if t[j+i] != wz[j]:
				k = False
				break
		if k:
			return i+1	

if __name__ == '__main__':
	print(wzorzec('lokomotywa','motyw'))
