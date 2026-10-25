from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_revc.txt'

with open(DATA_FILE, 'r') as f:
	dna = f.readline().rstrip()

reverse_complement = ''
for i in range(len(dna) - 1, -1, -1):
	if dna[i] == 'A':
		reverse_complement += 'T'
	elif dna[i] == 'C':
		reverse_complement += 'G'
	elif dna[i] == 'G':
		reverse_complement += 'C'
	elif dna[i] == 'T':
		reverse_complement += 'A'

print(reverse_complement)