#!/usr/bin/env python3

def dodaj(p,n,A,B):
    C = []
    tmp = 0
    for i in range(n-1,-1,-1):
        x,y = A[i], B[i]
        C.append((x+y+tmp) % p)
        tmp = (x+y+tmp) // p
    return C[::-1]

if __name__ == "__main__":
    print(dodaj(4,4,[3,1,2,2], [0,0,2,1]))
