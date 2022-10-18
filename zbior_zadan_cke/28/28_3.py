#!/usr/bin/env python3
# by neloduka_sobe

# Funkcja
def slaby_A_palindrom(s):
    if s == "A":
        return True
    elif len(s) % 2 ==0 and s[0] == s[-1]:
        if slaby_A_palindrom(s[:len(s)//2]) or slaby_A_palindrom(s[len(s)//2:]):
            return True
    return False

# Wywołanie
if __name__ == "__main__":
    print(slaby_A_palindrom("AABAABAA"))
    print(slaby_A_palindrom("ABBBABAA"))
    print(slaby_A_palindrom("ABAAAABA"))
    print(slaby_A_palindrom("AAAAAAAAAA"))
    print(slaby_A_palindrom("AAAABBBB"))
    print(slaby_A_palindrom("AAABBAAA"))

