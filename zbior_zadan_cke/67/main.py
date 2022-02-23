#!/usr/bin/env python3

fibo = [1,1]
for i in range(1,39):
    fibo.append(fibo[i] + fibo[i-1])

'''
### 67.1
print("Zadanie 67.1")
for i in range(9,40, 10):
    print(fibo[i])


### 67.2
print("Zadanie 67.2")
def is_prime(a):
    if a == 1:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

for i in fibo:
    if is_prime(i):
        print(i)

'''
### 67.3
#print("Zadanie 67.3 -> przepipować i do arkusza")
l = len(bin(fibo[-1])[2:])
for i in fibo:
    tmp = "0"*(l-len(bin(i)[2:])) + bin(i)[2:]
    print(*list(tmp), sep = ',')

'''
### 67.4
print("Zadanie 67.4")
for i in fibo:
    i = bin(i)[2:]
    if i.count("1") == 6:
        print(i)

    
    '''
