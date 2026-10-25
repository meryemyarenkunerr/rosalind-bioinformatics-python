from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_ini4.txt'

with open(DATA_FILE, 'r') as f:
	a, b = f.read().split()

a, b = int(a), int(b)

sum = 0
while a <= b:
	if a % 2 == 1:
		sum += a
	a += 1

print(sum)