#!/ur/bin/env python3

DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def szyfr(x):
	ret = ''
	for i in x:
		ret += DICT[i.upper()] + ' ' 
	return ret[:-1]

def deszyfr(x):
	ret = ''
	x = x.split(' ')
	for i in x:
		i = i.strip()
		print(i)
		ret += [y for y in DICT.keys() if DICT[y] == i][0]
	return ret


if __name__ == "__main__":
	s = 'test'
	s = szyfr(s)
	print(deszyfr(s))

