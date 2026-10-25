from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_ini6.txt'

with open(DATA_FILE, 'r') as f:
	string = f.read().split()

_dict = dict()

for word in string:
	if not word in _dict:
		_dict[word] = 1
	else:
		_dict[word] += 1

for key, value in _dict.items():
	print(key, value)