#!/usr/bin/env python3

def szyfr(k, W):
    ret = ''
    n = len(W)
    m = int(n/k)+1
    arr = [W[i:i+k+1] for i in range(0,n,m)]
    print(arr)
    for i in range(m):
        for y in arr:
            if len(y) > i:
                ret += y[i]
    return ret
if __name__ == "__main__":
    print(szyfr(3, 'SZYFROWANIE'))
