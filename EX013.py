cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         }


salario = float(input('Digite seu salário: '))

aumento = salario + (salario * 0.15)

print('O novo valor do seu salário é = {}R${}{} '.format(cores['amarelo'],aumento,cores['limpa']))