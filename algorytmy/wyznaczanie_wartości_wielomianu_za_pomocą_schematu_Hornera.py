#!/usr/bin/env python3
# by neloduka_sobe

### Wersja iteracyjna
def iteracyjna(arr, n, x):
    ret = arr[0]
    for i in range(1, n+1):
        ret = ret * x + arr[i]
    return ret

### Wersja rekurencyjna
def rekurencyjna(arr, n, x):
    if n == 0:
        return arr[0]
    return rekurencyjna(arr[:-1],n-1, x) * x + arr[n]

### Wywołanie
if __name__ == '__main__':
    print(iteracyjna([2,4,-3,7], 3, 3))
    print(rekurencyjna([2,4,-3,7], 3, 3))
