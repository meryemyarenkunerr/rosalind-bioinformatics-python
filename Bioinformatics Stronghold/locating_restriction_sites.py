from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_revp.txt'

def reverse_complement(seq: str) -> str:
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	return ''.join(complement[base] for base in reversed(seq))

def find_restriction_sites(dna: str) -> list[str]:
	n = len(dna)
	results = []

	for length in range(4, 13, 2):
		for i in range(n - length + 1):
			sub = dna[i:i + length]

			if sub == reverse_complement(sub):
				results.append((i + 1, length))

	return results


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		entries = f.read().strip().split('>')
		data = list()
		for entry in entries:
			if entry:
				lines = entry.strip().splitlines()
				sequence = ''.join(lines[1:])
				data.append(sequence)

	results = find_restriction_sites(data[0])
	for i, l in results:
		print(i, l)