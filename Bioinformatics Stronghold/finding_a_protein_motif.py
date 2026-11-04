from pathlib import Path
import requests
import re

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_mprt.txt'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/RosalindScript'}

def fetch_fasta(uniport_id):
	clean_id = uniport_id.split('_')[0].strip()
	url = 'https://www.uniprot.org/uniprot/' + clean_id + '.fasta'

	try:
			response = requests.get(url, headers)
			lines = response.text.splitlines()
			sequence = ''.join(
				line.strip() for line in lines if not line.startswith('>')
			)
			return sequence
	except Exception as e:
		print('AAAA')
		return None

def find_protein_motif(uniprot_ids):
	motif_pattern = re.compile(r'(?=(N[^P][ST][^P]))')
	for uniprot_id in uniprot_ids:
		uniprot_id = uniprot_id.strip()
		if not uniprot_id:
			continue

		sequence = fetch_fasta(uniprot_id)
		if not sequence:
			continue

		positions = [match.start() + 1
					 for match in motif_pattern.finditer(sequence)]
		if positions:
			print(uniprot_id)
			print(' '.join(map(str, positions)))

if __name__ == "__main__":
	with open(DATA_FILE, 'r') as f:
		data = []
		while True:
			line = f.readline().rstrip()
			if line:
				data.append(line)
			else:
				break

	find_protein_motif(data)