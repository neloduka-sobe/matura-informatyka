#!/usr/bin/env python3

def rle(s):
    ret = ''
    l = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            l += 1
        else:

            ret += ( str(l) if l > 1 else '' ) + s[i-1]
            l = 1

    ret += (str(l) if l > 1 else '') + s[i]
    return ret

if __name__ == "__main__":
    print("siiihhhjhddj")
    print(rle("siiihhhjhddj"))
