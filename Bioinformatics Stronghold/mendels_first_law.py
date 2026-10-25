from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / 'data' / 'rosalind_iprb.txt'

def factorial(number):
	result = 1
	for i in range(1, number + 1):
		result *= i
	return result

def combination(number, comb_factor):
	return factorial(number) / (factorial(comb_factor) * factorial(number - comb_factor))

def probability(k, m , n):
	population = k + m + n

	total_couples = combination(population, 2)

	# offsprings of 1/4 ratio with non-dominant phenotype
	heterozygous_couples = combination(m, 2)
	# no offspring with dominant phenotype
	recessive_couples = combination(n, 2)
	# offsprings of 1/2 ratio with non-dominant phenotype
	cross_couples = combination(m + n, 2) - heterozygous_couples - recessive_couples

	return 1 - (((recessive_couples) + (heterozygous_couples * 0.25) + (cross_couples * 0.5)) / (total_couples))


with open(DATA_FILE, 'r') as f:
	k, m, n = map(int, f.read().rstrip().split())

print(f'{probability(k, m ,n):.5f}')