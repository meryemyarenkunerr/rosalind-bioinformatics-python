from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_rear.txt'

def neighbors(p: str):
	n = len(p)
	for i in range(n):
		for j in range(i + 1, n):
			yield p[:i] + p[i:j + 1][::-1] + p[j + 1:]

def expand(frontier: str, visited: str) -> set:
	new_frontier = set()
	for p in frontier:
		for q in neighbors(p):
			if q not in visited:
				visited.add(q)
				new_frontier.add(q)

	return new_frontier

def reversal_distance(start: str, target: str) -> int:
	label = {v: i + 1 for i, v in enumerate(target)}
	start = tuple(label[x] for x in start)
	goal = tuple(range(1, len(start) + 1))

	if start == goal:
		return 0

	visited_a, visited_b = {start}, {goal}
	frontier_a, frontier_b = {start}, {goal}
	depth_a = depth_b = 0

	while True:
		if len(frontier_a) <= len(frontier_b):
			frontier_a = expand(frontier_a, visited_a)
			depth_a += 1
		else:
			frontier_b = expand(frontier_b, visited_b)
			depth_b += 1

		if visited_a & visited_b:
			return depth_a + depth_b


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		blocks = f.read().strip().split('\n\n')

	result = []
	for block in blocks:
		line_a, line_b = block.strip().splitlines()
		a = list(map(int, line_a.split()))
		b = list(map(int, line_b.split()))
		result.append(reversal_distance(a, b))

	print(*result)