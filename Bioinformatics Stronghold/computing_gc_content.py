from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_gc.txt'

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

header = ''
gc = -1
for i in range(len(data)):
	ratio = (data[i].count('G') + data[i].count('C')) / len(data[i]) * 100
	if ratio > gc:
		header = headers[i]
		gc = ratio

print(header)
print(gc)