from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_prot.txt'

codon_dict = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
			  'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
			  'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
			  'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
			  'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
			  'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
			  'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
			  'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
			  'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
			  'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
			  'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
			  'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
			  'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
			  'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
			  'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
			  'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

with open(DATA_FILE, 'r') as f:
	rna = f.read().rstrip()

codons = [rna[i:i + 3] for i in range(0, len(rna), 3)]

protein = ''
for codon in codons:
	if codon_dict[codon] == 'Stop':
		break
	protein += codon_dict[codon]

print(protein)