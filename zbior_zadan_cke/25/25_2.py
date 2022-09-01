#!/usr/bin/env python3

def zad25_2(slowo):
    l = 0
    r = len(slowo)-1
    teza = True

    while l <= r:
        if slowo[l] == ' ':
            l += 1
        if slowo[r] == ' ':
            r -= 1
        if slowo[l] != slowo[r]:
            teza = False
            break

        l += 1
        r -= 1

    return "TAK" if teza else "NIE"

print(zad25_2('ewo zeby tu byly buty bezowe'))
print(zad25_2('trafili popili fart'))
print(zad25_2('elf ukladal kufle'))
print(zad25_2('ewo ebytu byly buty bezowe'))
print(zad25_2('trafsilipopili fart'))
print(zad25_2('elf kladal kufle'))
