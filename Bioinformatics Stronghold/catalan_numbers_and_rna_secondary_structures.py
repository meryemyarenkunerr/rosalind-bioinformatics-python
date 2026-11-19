from pathlib import Path
from functools import lru_cache

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_cat.txt'

PAIRS = {('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G')}
MOD = 1_000_000

def count_matchings(s: str) -> int:
	@lru_cache(maxsize= None)
	def f(i, j):
		if i >= j:
			return 1
		if (j - i) % 2 == 1:
			return 0

		total = 0
		for k in range(i + 1, j, 2):
			if (s[i], s[k]) in PAIRS:
				total += f(i + 1, k) * f(k + 1, j)

		return total % MOD

	return f(0, len(s))


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		entries = f.read().strip().split('>')
		data = ''.join(entries[1].strip().splitlines()[1:])

	#print(data)
	print(count_matchings(data))

