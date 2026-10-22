with open('data/bioinformatics-stronghold/rosalind_hamm.txt', 'r') as f:
	s = f.readline().rstrip()
	t = f.readline().rstrip()

mutation_count = 0
for i in range(len(s)):
	if s[i] != t[i]:
		mutation_count += 1

print(mutation_count)