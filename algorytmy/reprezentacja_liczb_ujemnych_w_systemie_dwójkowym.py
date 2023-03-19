#!/usr/bin/env python3


# Znak Moduł
def zm(x):
	ret = ''
	if x < 0:
		ret += '1'
	else:
		ret += '0'
	ret += bin(abs(x))[2:]
	return ret

# U1
def u1(x):
	if x > 0:
		return bin(x)[2:]
	else:
		x += 127
		return '1' + bin(x)[2:]

def u1_2(x):
	ret = bin(abs(x))[2:] 
	ret = '0' *(8-len(ret)) + ret
	ret = ''.join(str(int(i) ^ 1) for i in ret)
	return ret
# U2
def u2(x):
	a = bin(abs(x))[2:]
	a = '0' *(8-len(a)) + a
	a = ''.join(str(int(i) ^ 1) for i in a)
	a = bin(int(a,2) + 1)[2:]
	return a
	

if __name__ == "__main__":
	print(zm(-10))
	print(u1(-10))
	print(u1_2(-106))
	print(u2(-21))
