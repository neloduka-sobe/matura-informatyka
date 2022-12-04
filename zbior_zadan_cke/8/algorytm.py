#!/usr/bin/env python3

def x(a, b, x):
    liczba = 0
    a = [0]+a
    b = [0]+b
    i = 1
    n = len(a)
    j = n-1
    while i <= n and j > 0:
        liczba += 1
        if a[i] + b[j] == x:
            return True, liczba
        elif a[i] + b[j] < x:
            i += 1
        else:
            j -= 1
    return False, liczba

if __name__ == "__main__":
    print(x([3,5,12,17],[8,10,13,14],21))
    print(x([4,6,8,10],[5,7,9,11],13))
    print(x([1,2,3,6,7],[11,12,14,15,16],20))
        

