dane = []
with open('Dane/pary.txt', 'r') as f:
	for i in f:
		dane.append([int(y) for y in i.strip().split(' ')])
# 2.4
print("Zad. 2.4")
for i in dane:
	x = max(i)
	y = min(i)
	if bin(y)[2:] == bin(x)[2:len(bin(y))]:
		print(y,x)
