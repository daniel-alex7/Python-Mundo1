cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         }

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

print('A média das notas é = {}{}{}'.format(cores['ciano'],media,cores['ciano']))