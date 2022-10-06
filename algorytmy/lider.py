#!/usr/bin/env python3
# by neloduka_sobe

### Funkcja
def lider(arr):
    lid = arr[0]
    ilosc = 0
    tmp = 1
    for i in range(1,len(arr)):
        if tmp == 0:
            lid = arr[i]
            tmp = 1
        elif arr[i] == lid:
            tmp += 1
        else:
            tmp -= 1
    if tmp == 0:
        return False
    else:
        for i in arr:
            if i == lid:
                ilosc += 1
        
        if len(arr) // 2 < ilosc:
            return lid
        return False


### Wywołanie
if __name__ == '__main__':
    print(lider([2,2,2,2,2,4,6,7,8]))

