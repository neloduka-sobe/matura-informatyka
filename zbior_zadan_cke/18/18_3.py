#!/usr/bin/env python3

### Rekurencyjnie
def NWD(arr):
    if len(arr) == 2:
        a, b = arr
        while b != 0:
            a,b = b, a%b
        return a
    return NWD([NWD(arr[:2])] + arr[2:])

### Iteracyjnie
def NWD1(a,b):
    while b != 0:
        a,b = b, a % b
    return a

def NWD2(arr):
    i = arr[0]
    for y in range(1,len(arr)):
        i = NWD1(i, arr[y])
    return i



if __name__ == "__main__":
    print(NWD([36, 24, 72, 150]))
    print(NWD([121, 330, 990, 1331, 110, 225]))
    print(NWD([119, 187, 323, 527, 731]))

    print(NWD2([36, 24, 72, 150]))
    print(NWD2([121, 330, 990, 1331, 110, 225]))
    print(NWD2([119, 187, 323, 527, 731]))
