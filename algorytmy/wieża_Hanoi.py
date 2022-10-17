#!/usr/bin/env python3
# by neloduka_sobe

# Wersja rekurencyjna
def hanoi_rek(a,b,c,n):
    if n > 0:
        hanoi_rek(a,c,b,n-1)
        print(a, "na", b)
        hanoi_rek(c,b,a,n-1)

# Wersja iteracyjna
def hanoi_iter(a,b,c, n):
    paliki = [a,b,c]
    krazki = [0 for i in range(n)]
    while krazki.count(0) != 0 or krazki.count(2) != 0:
        if n % 2 == 0:
            tmp = (krazki[0] - 1) if (krazki[0] - 1) >= 0 else 2
            print(paliki[krazki[0]], 'na', paliki[tmp])
            krazki[0] = tmp

        else:
            tmp = (krazki[0] + 1) % 3
            print(paliki[krazki[0]], 'na', paliki[tmp])
            krazki[0] = tmp

        for i in range(len(krazki)):
            if krazki[i] != krazki[0]:
                tmp = krazki[i]
                while krazki[i] in (tmp, krazki[0]):
                    krazki[i] += 1 
                    krazki[i] %= 3
                print(paliki[tmp], 'na', paliki[krazki[i]])
                break

if __name__ == "__main__":
    hanoi_rek('a', 'b', 'c', 4)
    print()
    hanoi_iter('a', 'b', 'c', 4)
