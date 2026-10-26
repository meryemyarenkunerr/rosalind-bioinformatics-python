from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_subs.txt'

def finding_occurences_naive(s, t):
	occurences = []
	len_s, len_t = len(s), len(t)

	for i in range(len_s - len_t + 1):
		match = True
		for j in range(len_t):
			if s[i + j] != t[j]:
				match = False
				break
		if match:
			occurences.append(i + 1)
	return occurences


with open(DATA_FILE, 'r') as f:
	s = f.readline().rstrip()
	t = f.readline().rstrip()

result = finding_occurences_naive(s, t)
for i in result:
	print(i, end= ' ')
