from pathlib import Path
import itertools

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_long.txt'

def overlap(a, b, min_length= 3):
	start = 0
	while True:
		start = a.find(b[:min_length], start)
		if start == -1:
			return 0

		if b.startswith(a[start:]):
			return len(a) - start

		start += 1

def pick_maximal_overlap(reads, k):
	reada, readb = None, None
	best_olen = 0
	for a, b in itertools.permutations(reads, 2):
		olen = overlap(a, b, min_length= k)
		if olen > best_olen:
			reada, readb = a, b
			best_olen = olen
	return reada, readb, best_olen

def greedy_scs(reads, k):
	read_a, read_b, olen = pick_maximal_overlap(reads, k)
	while olen > 0:
		reads.remove(read_a)
		reads.remove(read_b)
		reads.append(read_a + read_b[olen:])
		read_a, read_b, olen = pick_maximal_overlap(reads, k)
	return ''.join(reads)


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		entries = f.read().strip().split('>')
		data = list()
		for entry in entries:
			if entry:
				lines = entry.strip().splitlines()
				sequence = ''.join(lines[1:])
				data.append(sequence)

		print(greedy_scs(data, len(data[0]) // 2))