data = open('data/python-village/rosalind_ini2.txt', 'r')
a, b = data.read().split()

a = int(a)
b = int(b)

print(a**2 + b**2)