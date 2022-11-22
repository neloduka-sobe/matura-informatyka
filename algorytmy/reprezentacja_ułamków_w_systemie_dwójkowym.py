#!/usr/bin/env python3
# by neloduka_sobe
# źródło: http://smurf.mimuw.edu.pl/node/477

def zamiana(n, d):
    ret = '0.'
    n *= 2
    while d != 0  and n != 0:
        if n < 1:
            ret += '0'
        else:
            ret += '1'
            n -= 1
        d -= 1
        n *= 2
    return ret

if __name__ == '__main__':
    print(zamiana((1/2), 2))
