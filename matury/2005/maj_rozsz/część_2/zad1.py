#!/usr/bin/env python3


# do podpunktu a)
with open('zad4a.txt', 'a') as f:
    for n in range(1, 7001):
        cena_d1 = 0.01*n
        cena_d2 = 0.5*(n**0.5)
        m = 0.0001*n
        czas_d1 = 10*m**3 + 7*m**2 + 0.1*m + 0.1
        czas_d2 = 5 * czas_d1

        if (cena_d1+czas_d1) > (cena_d2+czas_d2):
            f.write(f"Dla {n=} D2\n")
        else:
            f.write(f"Dla {n=} D1\n")
        if n in (100, 1000, 5000):
            f.write(f"Koszt D1: {cena_d1+czas_d1}; Koszt D2: {cena_d2+czas_d2}\n")

# do podpunktu b)
with open('zad4b.csv', 'a') as f:
    for n in range(6000, 9001, 100):
        cena_d2 = 0.5*(n**0.5)
        m = 0.0001*n
        czas_d2 = 5* (10*m**3 + 7*m**2 + 0.1*m + 0.1)
        f.write(f'{n}; {cena_d2}; {czas_d2}\n'.replace('.',','))
    
