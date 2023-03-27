# Zadanie 2. c)
def z2(x,y,n):
    if x > (n//2):
            x = abs(x-n-1)
    if y > (n//2):
            y = abs(y-n-1)
    return 3*(n-1) + 2*((abs(y-1) if x > y else abs(x-1)))

