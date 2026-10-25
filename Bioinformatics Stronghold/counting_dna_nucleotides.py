from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_revc.txt'

with open(DATA_FILE, 'r') as f:
	data = f.read().rstrip()

count_dict = dict()

for i in data:
	if not i in count_dict:
		count_dict[i] = 1
	else:
		count_dict[i] += 1

print(count_dict['A'], count_dict['C'], count_dict['G'], count_dict['T'])

## with collections module
#import collections

#counter = collections.Counter(data)
#print(counter['A'], counter['C'], counter['G'], counter['T'])