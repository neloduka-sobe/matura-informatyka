#!/usr/bin/env python3
# by neloduka_sobe

def euklides1(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def euklides2(a,b):
    while b != 0:
        a, b = b, a%b 
    return a

if __name__ == '__main__':
    print(euklides1(3, 2137))
    print(euklides2(3, 2137))
    print(euklides1(144, 12*1423))
    print(euklides2(144, 12*1423))
