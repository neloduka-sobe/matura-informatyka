#!/usr/bin/env python3
# by neloduka_sobe

def przestawienie_kolumnowe(s, k):
    n, dl = len(k), len(s)
    if dl % n:
        m = dl // n +1
    else:
        m = dl // n
    arr = [['' for i in range(n)] for _ in range(m)]
    
    f = 0
    for i in range(m):
        for y in range(n):
            if f < dl:
                arr[i][y] = s[f]
                f += 1

    ret = ''
    for z in k:
        for q in range(m):
            ret += arr[q][z]

    return ret

if __name__ == '__main__':
    print(przestawienie_kolumnowe("KRYPTOANALIZA", [2,1,4,0,3]))
