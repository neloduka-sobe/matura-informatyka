#!/usr/bin/env python3
# by neloduka_sobe

# Funkcja
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Wywołanie
if __name__ == "__main__":
    print(is_prime(2137))
    print(is_prime(2))
    print(is_prime(13))
    print(is_prime(25))
    print(is_prime(1))
