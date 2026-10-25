from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_ini2.txt'

with open(DATA_FILE, 'r') as f:
	a, b = map(int, f.read().split())

print(a**2 + b**2)