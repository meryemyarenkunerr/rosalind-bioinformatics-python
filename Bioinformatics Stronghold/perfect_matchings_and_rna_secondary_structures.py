from pathlib import Path
from math import factorial

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_pmch.txt'


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		entries = f.read().strip().split('>')
		rna = ''
		for entry in entries:
			if entry:
				lines = entry.strip().splitlines()
				sequence = ''.join(lines[1:])
				rna += sequence

	print(factorial(rna.count('A')) * factorial(rna.count('C')))