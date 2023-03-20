#!/usr/bin/env python3

def func(a):
	s = []
	for i in a.split():
		if i not in '*+/-':
			s.append(int(i))
		else:
			x = s.pop(-1)
			y = s.pop(-1)
			if i == "*":
				s.append(x*y)
			elif i == "+":
				s.append(x+y)
			elif i == "/":
				s.append(y/x)
			elif i == "-":
				s.append(y-x)
	return s

if __name__ == "__main__":
	print(func("12 2 3 4 * 10 5 / + * +"))
	print(func("5 1 2 + 4 * + 3 -"))
