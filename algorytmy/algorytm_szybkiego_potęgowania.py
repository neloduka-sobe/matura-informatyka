#!/usr/bin/env python3
# by neloduka_sobe

# Wersja iteracyjna
def iter(a,n):
    ret = 1
    while n > 0:
        if n%2 == 1:
            ret *= a
        a *= a
        n //= 2
    return ret

# Wersja rekurencyjna
def rek(a,n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    if n | 1 > n:
        return rek(a,n//2) * rek(a,n//2)
    return rek(a, n//2) * rek(a, n//2) * a


# Wywołanie
if __name__ == '__main__':
    for i in range(2,10):
        for y in range(2,100):
            print(f'iter: {y}^{i}; {iter(y,i) == y**i}')
            print(f'rek: {y}^{i}; {rek(y,i) == y**i}')
            print(f"{rek(y,i)==iter(y,i)=}")
