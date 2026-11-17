from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_pper.txt'

def partial_permutation(n: int, k: int) -> int:
	result = 1
	for i in range(n, n - k, -1):
		result *= i

	return result % 1000000


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		n, k = map(int, f.read().rstrip().split())

	print(partial_permutation(n, k))
