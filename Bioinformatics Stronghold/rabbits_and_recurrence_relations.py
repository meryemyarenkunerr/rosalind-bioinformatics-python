with open('data/bioinformatics-stronghold/rosalind_fib.txt', 'r') as f:
	n, k = map(int, f.read().split())

adult = 0
juvenile = 1
print(f'month 1 -- adult: {adult} -- juvenile: {juvenile}')
for month in range(2, n + 1):
	temp = adult
	adult += juvenile
	juvenile = temp * k
	print(f'month {month} -- adult: {adult} -- juvenile: {juvenile}')

print(f"Total number of Rabbits: {adult + juvenile}")