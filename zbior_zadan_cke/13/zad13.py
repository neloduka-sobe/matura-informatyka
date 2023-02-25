#!/usr/bin/env python3

def x(px, py, ax, ay):
    n = len(px)
    for i in range(0, n):
        roznicax = px[i] - ax
        roznicay = py[i] - ay
        drugix = ax - roznicax
        drugiy = ay - roznicay
        znaezione = False
        for k in range(0, n):
            if drugix == px[k] and drugiy == py[k]:
                znalezione = True
        if not znalezione:
            return "NIE"
    return "TAK" 

if __name__ == "__main__":
    print(x([-1,-2,1,-1,2,1,0],[4,2,2,0,0,-2,1],0,1))

