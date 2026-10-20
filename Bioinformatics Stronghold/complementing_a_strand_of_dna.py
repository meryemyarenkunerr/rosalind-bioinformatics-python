dna = open('data/bioinformatics-stronghold/rosalind_revc.txt').read()

reverse_complement = ''
for i in range(len(dna) - 1, -1, -1):
	if dna[i] == 'A':
		reverse_complement += 'T'
	elif dna[i] == 'C':
		reverse_complement += 'G'
	elif dna[i] == 'G':
		reverse_complement += 'C'
	elif dna[i] == 'T':
		reverse_complement += 'A'

print(reverse_complement)