from pathlib import Path
import itertools

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_grph.txt'


with open(DATA_FILE, 'r') as f:
	headers = []
	data = []
	line = f.readline().rstrip()
	while True:
		if not line:
			break
		if line[0] == '>':
			headers.append(line[1:])
			entry = ''
			while True:
				line = f.readline().rstrip()
				if not line or line[0] == '>':
					break
				entry += line
			data.append(entry)

overlap_set = set()
for i in range(len(data)):
	prefix = data[i][:3]
	for j in range(len(data)):
		if j == i:
			continue
		suffix = data[j][len(data[j]) - 3:]
		if suffix == prefix:
			overlap_set.add((j, i))


for i in overlap_set:
	h, t = i
	print(headers[h], headers[t])