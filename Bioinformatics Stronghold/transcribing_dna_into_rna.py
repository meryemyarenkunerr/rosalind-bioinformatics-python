from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_rna.txt'

dna = open(DATA_FILE, 'r').read().strip()

rna = ''
for i in dna:
	if i == 'T':
		rna += 'U'
	else:
		rna += i

print(rna)
