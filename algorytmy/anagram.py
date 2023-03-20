#!/usr/bin/env python3

def anagram_1(x,y):
	x = ''.join(i for i in x if i.isalpha())
	y = ''.join(i for i in y if i.isalpha())
	return sorted(x) == sorted(y)

def anagram_2(x,y):
	d = {}
	for i in x:
		if i.isalpha():
			d.setdefault(i, 0)
			d[i] += 1
	for i in y:	
		if i.isalpha():
			if i not in d.keys():
				return False
			else:
				d[i] -= 1
				if d[i] < 0:
					return False
	return True

if __name__ == "__main__":
	print(anagram_1("jim morrison", "mr mojo risin"))
	print(anagram_2("jim mor,.,.rison", "mr mojo risin"))
