even_lines = []

with open('data/python-village/rosalind_ini5.txt', 'r') as f:
	while True:
		f.readline()
		even_line = f.readline().rstrip()
		if len(even_line) == 0:
			break

		even_lines.append(even_line)

for line in even_lines:
	print(line)