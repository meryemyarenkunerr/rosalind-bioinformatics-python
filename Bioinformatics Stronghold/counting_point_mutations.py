from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_hamm.txt'

with open(DATA_FILE, 'r') as f:
	s = f.readline().rstrip()
	t = f.readline().rstrip()

mutation_count = 0
for i in range(len(s)):
	if s[i] != t[i]:
		mutation_count += 1

print(mutation_count)