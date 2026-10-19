dna = open('data/bioinformatics-stronghold/rosalind_rna.txt', 'r').read().strip()

rna = ''
for i in dna:
	if i == 'T':
		rna += 'U'
	else:
		rna += i

print(rna)
