from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_iev.txt'

def probabilities(index):
	if index == 1 or index == 2 or index == 3:
		return 1
	elif index == 4:
		return 0.75
	elif index == 5:
		return 0.5
	elif index == 6:
		return 0


with open(DATA_FILE, 'r') as f:
	genotypes = list(map(int, f.read().rstrip().split()))

expected_offspring = 0
for i in range(len(genotypes)):
	expected_offspring += genotypes[i] * probabilities(i + 1) * 2

print(expected_offspring)