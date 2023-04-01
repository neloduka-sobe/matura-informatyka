#!/usr/bin/env python3

slowa = []

with open("dane/slowa.txt","r") as f:
	for i in f:
		slowa.append(i.strip())

# a)
with open('hasla_a.txt','w+') as f:
	for i in slowa:
		f.write(f"{i[::-1]}\n")

print("a)")
print(max(slowa, key=len)[::-1],len(max(slowa, key=len)))
print(min(slowa, key=len)[::-1],len(min(slowa, key=len)))

# b)
print("b)")
ma = 0
ma_w = ''
mi = float('inf')
mi_w = ''
suma = 0
with open('hasla_b.txt','w+') as f:
	for i in slowa:
		for y in range(len(i), -1,-1):
			if i[:y] == i[:y][::-1]:
				t = i[y:][::-1]+i
				f.write(f"{t}\n")

				if len(t) == 12:
					print(t)
				if len(t) > ma:
					ma = len(t)
					ma_w = t
				elif len(t) < mi:
					mi = len(t)
					mi_w = t
				suma += len(t)
				break

	print(f"Maks: {ma} dla {ma_w}")	
	print(f"Min: {mi} dla {mi_w}")	
	print(f"Suma: {suma}")

			
