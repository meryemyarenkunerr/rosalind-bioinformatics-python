from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_cons.txt'


if __name__ == "__main__":
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

	t_data = list(zip(*data))
	profile = [[i.count('A'), i.count('C'), i.count('G'), i.count('T')] for i in t_data]
	t_profile = list(zip(*profile))

	for n in range(len(profile)):
		if profile[n].index(max(profile[n])) == 0:
			print('A', end='')
		elif profile[n].index(max(profile[n])) == 1:
			print('C', end='')
		elif profile[n].index(max(profile[n])) == 2:
			print('G', end='')
		elif profile[n].index(max(profile[n])) == 3:
			print('T', end='')
		if n == len(profile) - 1:
			print()

	print('A: ', end= '')
	for i in t_profile[0]:
		print(i, end=' ')
	print()

	print('C: ', end= '')
	for i in t_profile[1]:
		print(i, end=' ')
	print()

	print('G: ', end= '')
	for i in t_profile[2]:
		print(i, end=' ')
	print()

	print('T: ', end= '')
	for i in t_profile[3]:
		print(i, end=' ')
	print()

