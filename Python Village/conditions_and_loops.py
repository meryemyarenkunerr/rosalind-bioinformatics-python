a, b = open('data/python-village/rosalind_ini4.txt', 'r').read().split()

a, b = int(a), int(b)

sum = 0
while a <= b:
	if a % 2 == 1:
		sum += a
	a += 1

print(sum)