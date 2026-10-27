from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_fibd.txt'

with open(DATA_FILE, 'r') as f:
	n, m = map(int, f.read().split())


new_juveniles = [0] * (n + 1)

adult = 0
juvenile = 1
new_juveniles[1] = juvenile
for month in range(2, n + 1):
	temp = adult
	adult += juvenile - new_juveniles[month - m]
	juvenile = temp
	new_juveniles[month] = juvenile

print(adult + juvenile)