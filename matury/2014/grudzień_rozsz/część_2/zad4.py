#!/usr/bin/env python3
import math

def f(r,t,T):
	x = r * math.sin(2*t*math.pi/T)
	y = r * math.cos(2*t*math.pi/T)
	return x,y

# 4.1
for t in range(3*100, int(12.5*100)+1, 5):
	t /= 100
	x,y = f(5,t,12.5)
	if y > x:
		print(f"4.1: {t} (czas od początku ruchu mrówki)")
		break

# 4.2
v = 1
T = 10
dt = 0.5
with open('wykres.csv','w') as file:
	file.write("x;y\n")
	for t in range(int(0.5*10), int(T*10)+1, 5):
		t /= 10
		r = v*t
		x,y = f(r,t,T)
		file.write(f"{x};{y}\n")
print("4.2: W pliku wykres.ods")
	
# 4.3
suma = 0
v = 1
T = 10
dt = 0.5
last = (0,0)
for t in range(int(0.5*10), int(T*10)+1, 5):
	t /= 10
	r = v*t
	x,y = f(r,t,T)
	suma += math.sqrt((x-last[0])**2 + (y-last[1])**2)
	last = [x,y]

print(f"4.3: {round(suma,4)}0")
