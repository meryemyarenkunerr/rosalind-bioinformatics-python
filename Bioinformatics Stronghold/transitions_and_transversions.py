from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_tran.txt'

PURINES = ['A', 'G']
PYRIMIDINES = ['T', 'C']

if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		entries = f.read().strip().split('>')
		data = list()
		for entry in entries:
			if entry:
				lines = entry.strip().splitlines()
				sequence = ''.join(lines[1:])
				data.append(sequence)

	s1 = data[0]
	s2 = data[1]

	transition = 0
	transversions = 0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			continue
		elif s1[i] == 'A' and s2[i] == 'G':
			transition += 1
		elif s1[i] == 'G' and s2[i] == 'A':
			transition += 1
		elif s1[i] == 'T' and s2[i] == 'C':
			transition += 1
		elif s1[i] == 'C' and s2[i] == 'T':
			transition += 1
		else:
			transversions += 1

	print(f'{transition / transversions:.11f}')