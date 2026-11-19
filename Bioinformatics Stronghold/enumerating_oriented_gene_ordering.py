from pathlib import Path
from itertools import permutations, product
from math import factorial

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_sign.txt'


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		num = int(f.readline().rstrip())

	print(factorial(num) * 2 ** num)
	for perm in permutations(range(1, num + 1)):
		for signs in product([1, -1], repeat= num):
			print(*[p * s for p, s in zip(perm, signs)])
