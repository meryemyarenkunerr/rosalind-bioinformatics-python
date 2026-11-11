from pathlib import Path
from itertools import product

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_lexf.txt'


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		alphabet = f.readline().rstrip().split()
		n = int(f.readline().rstrip())

	for i in product(alphabet, repeat= n):
		print(''.join(i))
