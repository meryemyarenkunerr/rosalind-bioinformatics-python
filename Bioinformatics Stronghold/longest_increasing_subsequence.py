from pathlib import Path
from bisect import bisect_left

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_lgis.txt'

def lis(seq: str) -> list[int]:
	tails = list()
	tails_idx = list()
	parent = [-1] * len(seq)

	for i, x in enumerate(seq):
		pos = bisect_left(tails, x)

		if pos == len(tails):
			tails.append(x)
			tails_idx.append(i)
		else:
			tails[pos] = x
			tails_idx[pos] = i

		parent[i] = tails_idx[pos - 1] if pos > 0 else -1

	result = list()
	i = tails_idx[-1]
	while i != -1:
		result.append(seq[i])
		i = parent[i]

	return result[::-1]


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		n = int(f.readline())
		perm = list(map(int, f.readline().split()))

	print(*lis(perm))
	print(*[-x for x in lis([-x for x in perm])])

