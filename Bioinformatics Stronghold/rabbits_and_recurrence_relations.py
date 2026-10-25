from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_fib.txt'

with open(DATA_FILE, 'r') as f:
	n, k = map(int, f.read().split())

adult = 0
juvenile = 1
for month in range(2, n + 1):
	temp = adult
	adult += juvenile
	juvenile = temp * k

print(adult + juvenile)