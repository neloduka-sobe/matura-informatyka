#!/usr/bin/env python3
# by neloduka_sobe
from algorytm_Euklidesa import euklides2
from random import randint

def wzglednie_pierwsza(x):
    while True:
        y = randint(1,10000)
        #y = 17 #użyte do testów - 
        if euklides2(x,y) == 1:
            return y

def gen_d(p,q,e):
    while True:
        d = randint(1,10000)
        #d = 2753 #użyte do testów
        if (e*d) % ((p-1)*(q-1)) == 1:
            return d
    
def gen_klucz(p,q):
    n = p*q
    e = wzglednie_pierwsza((p-1)*(q-1))
    d = gen_d(p,q,e) 
    return (d,n), (e,n)

if __name__ == "__main__":
    print(gen_klucz(61,53))
