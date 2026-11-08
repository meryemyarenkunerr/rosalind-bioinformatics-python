from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_lcsm.txt'

def find_shared_motif(dna_list: list) -> str:
	shortest_dna = min(dna_list, key= len)
	others = [dna for dna in dna_list if dna != shortest_dna]

	for length in range(len(shortest_dna), 0, -1):
		for start in range(len(shortest_dna) - length + 1):
			substr = shortest_dna[start:start + length]
			if all(substr in dna for dna in others):
				return substr

	return ''


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		entries = f.read().strip().split('>')
		data = list()
		for entry in entries:
			if entry:
				lines = entry.strip().splitlines()
				sequence = ''.join(lines[1:])
				data.append(sequence)

	print(find_shared_motif(data))