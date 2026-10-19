data = open('data/bioinformatics-stronghold/rosalind_dna.txt', 'r').read().rstrip()

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