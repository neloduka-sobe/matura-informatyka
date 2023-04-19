#!/usr/bin/env python3

def t(n):
	trojkat = [[0,1,0]]

	for i in range(1,n):
		z = trojkat[i-1]
		add = [0]
		for y in range(1,len(z)):
			add.append(z[y-1]+z[y])
		add.append(0)
		trojkat.append(add)
	return [i[1:-1] for i in trojkat]


pascal = t(30)

# a)
print("a)")
for ind,i in enumerate(pascal):
	if ind in (9,19,29):
		print(ind+1, max(i))	

# b)
print("\nb)")
for ind,i in enumerate(pascal):
	print(ind+1, len(''.join(map(str, i))))	

# c)
print("\nc)")
for ind,i in enumerate(pascal):
	if not any(map(lambda x: x%5==0, i)):
		print(ind+1)

# d)
print('\nd) (Także w pliku fraktal.csv)')
with open('fraktal.csv','w') as f:
	for i in pascal:
		print(''.join(map(lambda x: 'X' if x%3==0 else ' ',i)))
		f.write(';'.join(map(lambda x: 'X' if x%3==0 else ' ',i))+'\n')
