#!/usr/bin/env python3
# by neloduka_sobe

def max_w_zbiorze(a:list):
    m = a[0]
    for i in a:
        if i > m:
            m = i
    return m

def min_w_zbiorze(a:list):
    m = a[0]
    for i in a:
        if i < m:
            m = i
    return m

if __name__ == "__main__":
    # Z funkcji wbudowanych
    a = set(i for i in range(999))
    # max
    print(max(a))

    # min
    print(min(a))

    # Z napisanych funkcji
    b = list(a)
    # max
    print(max_w_zbiorze(b))

    # min
    print(min_w_zbiorze(b))
