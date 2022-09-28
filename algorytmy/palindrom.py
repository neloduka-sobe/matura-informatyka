#!/usr/bin/env python3
# by neloduka_sobe

### Funkcje
def palindrom_1(s):
    return s == s[::-1]

def palindrom_2(s):
    """Wersja usuwająca spacje"""
    s = s.replace(' ', '')
    return s == s[::-1]

# Wersja z lambdą
palindrom_3 = lambda s: s == s[::-1]

def palindrom_4(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

### Wywołanie
if __name__ == "__main__":
    for i in ('kajak', 'ela', 'tak', 'milim', 'allla', 'alla'):
        print(i)
        print(palindrom_1(i))
        print(palindrom_2(i))
        print(palindrom_3(i))
        print(palindrom_4(i))

