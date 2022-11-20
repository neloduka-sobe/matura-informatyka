#!/usr/bin/env python3

def rownowazne(x,y):
    ilosc_x = {i:0 for i in "ABCDERFGHIJ"}
    ilosc_y = {i:0 for i in "ABCDERFGHIJ"}
    if len(x) == len(y):
        for i in x:
            ilosc_x[i] += 1
        for i in y:
            ilosc_y[i] += 1
        for i in zip(ilosc_x.values(), ilosc_y.values()):
            if i[0] != i[1]:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    print(rownowazne("ABCA", "BCAA"))
    print(rownowazne("ABCA", "ABCC"))
