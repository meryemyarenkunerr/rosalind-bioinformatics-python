from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_ini3.txt'

with open(DATA_FILE, 'r') as file:
	text = file.readline().rstrip()
	a, b, c, d = file.readline().split()

	a, b, c, d = int(a), int(b), int(c), int(d)

substring1 = text[a:b + 1]
substring2 = text[c:d + 1]

print(substring1, substring2)