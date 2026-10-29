from pathlib import Path
import math

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_lia.txt'

with open(DATA_FILE, 'r') as f:
	k, N = map(int, f.read().rstrip().split())

total_org = 2 ** k
prob = 0
for i in range(N, total_org + 1):
	prob += math.comb(total_org, i) * ((1/4) ** i) * ((3/4) ** (total_org - i))

print(f'{prob:.3f}')