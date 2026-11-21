from pathlib import Path
from collections import Counter

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_corr.txt'

COMP = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def revcomp(s: str) -> str:
	return ''.join(COMP[c] for c in reversed(s))

def canonical(s: str) -> str:
	return min(s, revcomp(s))

def read_fasta(path):
	with open(path) as f:
		entries = f.read().strip().split('>')
	return [''.join(e.strip().splitlines()[1:]) for e in entries if e]

def hamming(a: str, b: str) -> int:
	return sum(x != y for x, y in zip(a, b))


if __name__ == '__main__':
	reads = read_fasta(DATA_FILE)
	counts = Counter(canonical(r) for r in reads)

	correct = {r for r in reads if counts[canonical(r)] >= 2}
	wrong = [r for r in reads if counts[canonical(r)] == 1]

	candidates = correct | {revcomp(r) for r in correct}
	for w in wrong:
		for c in candidates:
			if hamming(w, c) == 1:
				print(f'{w}->{c}')
				break
