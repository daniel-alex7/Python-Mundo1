cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         }

n1 = int(input('Digite um número '))
n2 = int(input('Digite um número '))
soma = (n1 + n2)
print('A soma é = {}{}{}'.format(cores['amarelo'],soma,cores['amarelo']))
