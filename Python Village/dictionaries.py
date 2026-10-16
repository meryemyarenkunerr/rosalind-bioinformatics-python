string = open('data/python-village/rosalind_ini6.txt', 'r').read().split()

_dict = dict()

for word in string:
	if not word in _dict:
		_dict[word] = 1
	else:
		_dict[word] += 1

for key, value in _dict.items():
	print(key, value)