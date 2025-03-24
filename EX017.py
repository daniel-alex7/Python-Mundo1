from math import pow, sqrt

n1 = float(input('Digite o primeiro cateto: '))
n2 = float(input('Digite o primeiro cateto: '))

hip = (sqrt(pow(n1,2) + pow(n2,2)))

print('A soma dos catetos {} e {} é igual à: {}'.format(n1,n2,hip))