#!/usr/bin/env python3

def f(M,N, A):
    T = [0 for i in range(N)]
    for i in range(1, M+1):
        j = i
        while j < N+1:
            T[j] = 1
            j += A[i]
    return T
