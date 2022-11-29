#!/usr/bin/env python3

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return "Nie"
    return "Tak"

if __name__ == "__main__":
    print(is_prime(2))
    print(is_prime(13))
    print(is_prime(11))
    print(is_prime(12))
