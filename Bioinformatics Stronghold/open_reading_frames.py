from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_orf.txt'

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

translate = str.maketrans('ATCG', 'TAGC')

def reverse_complement_rna(dna: str) -> str:
	return dna.translate(translate)[::-1].replace('T', 'U')

def find_orfs(rna: str) -> set[str]:
	proteins = set()
	length = len(rna)

	for i in range(length - 2):
		if rna[i:i + 3] == 'AUG':
			protein_chars = []
			stopped = False

			for j in range(i, length - 2, 3):
				aa = codon_dict.get(rna[j:j + 3])

				if aa == 'Stop':
					stopped = True
					break
				elif aa is None:
					break

				protein_chars.append(aa)

			if stopped:
				proteins.add(''.join(protein_chars))

	return proteins


if __name__ == '__main__':
	with open(DATA_FILE, 'r') as f:
		lines = [line.rstrip() for line in f if not line.startswith('>')]
		dna = ''.join(lines)

	rna_reverse = reverse_complement_rna(dna)
	rna_forward = dna.replace('T', 'U')

	all_proteins = find_orfs(rna_forward) | find_orfs(rna_reverse)
	for i in all_proteins:
		print(i)