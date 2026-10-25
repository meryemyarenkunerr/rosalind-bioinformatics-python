from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_ini5.txt'

even_lines = []
with open(DATA_FILE, 'r') as f:
	while True:
		f.readline()
		even_line = f.readline().rstrip()
		if len(even_line) == 0:
			break

		even_lines.append(even_line)

for line in even_lines:
	print(line)