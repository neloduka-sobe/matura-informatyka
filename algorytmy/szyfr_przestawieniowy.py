#!/usr/bin/env python3
'''
https://www.algorytm.edu.pl/algorytmy-maturalne/szyfr-przestawieniowy.html
'''

def szyfr(x):
	samogloski = ('a', 'e', 'i', 'o', 'u', 'y')	
	ret = ["" for i in range(len(x))]
	last = ''
	f = -1
	for ind, i in enumerate(x):
		if i in samogloski:
			ret[ind] = i
		else:
			if f > -1:
				ret[ind] = last 
				last = i
			else:
				f = ind
				last = i
	if f > -1:
		ret[f] = last
	return ''.join(ret)

if __name__ == "__main__":
	print(szyfr("lokomotywa"))
