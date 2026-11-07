from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_splc.txt'

codon_dict = {
	'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
	'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
	'AAU': 'N', 'AAC': 'N',
	'GAU': 'D', 'GAC': 'D',
	'UGU': 'C', 'UGC': 'C',
	'CAA': 'Q', 'CAG': 'Q',
	'GAA': 'E', 'GAG': 'E',
	'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
	'CAU': 'H', 'CAC': 'H',
	'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
	'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
	'AAA': 'K', 'AAG': 'K',
	'AUG': 'M',
	'UUU': 'F', 'UUC': 'F',
	'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
	'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
	'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
	'UGG': 'W',
	'UAU': 'Y', 'UAC': 'Y',
	'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
	'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		entries = f.read().strip().split('>')
		data = list()
		for entry in entries:
			if entry:
				lines = entry.strip().splitlines()
				sequence = ''.join(lines[1:])
				data.append(sequence)

	dna = data[0]
	introns = data[1:]

	for intron in introns:
		dna = dna.replace(intron, '')

	mrna = dna.replace('T', 'U')

	protein = ''

	start_index = mrna.find('AUG')
	if start_index != -1:
		codons = [mrna[i:i + 3] for i in range(start_index, len(mrna), 3)]
		for codon in codons:
			aa = codon_dict.get(codon)
			if aa == 'Stop':
				break
			protein += aa

	print(protein)
