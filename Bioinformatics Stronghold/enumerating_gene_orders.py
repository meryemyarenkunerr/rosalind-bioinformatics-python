from pathlib import Path
import itertools

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_perm.txt'

def factorial(num):
	if num == 0:
		return 1
	return num * factorial(num - 1)



with open(DATA_FILE, 'r') as f:
	num = int(f.readline().rstrip())

print(factorial(num))

permutations = list(itertools.permutations([i for i in range(1, num + 1)]))
for i in permutations:
	for j in i:
		print(j, end= ' ')
	print()