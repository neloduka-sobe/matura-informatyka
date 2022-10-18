#!/usr/bin/env python3
# by neloduka_sobe

# Importownie funkcji do generowania kluczy
from RSA_generowanie_kluczy import gen_klucz

# Funkcje
def RSA_szyfr(e, n, t):
    a = [(ord(i)**e) % n for i in t]
    return ''.join(chr(i) for i in a)

# Wywołanie
if __name__ == "__main__":
    (d, n), (e, n) = gen_klucz(61,53)

    print(d,n,e,n)

    t = RSA_szyfr(e, n, "Tak było")
    print(RSA_szyfr(d,n,t))
