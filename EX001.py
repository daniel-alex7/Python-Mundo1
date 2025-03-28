cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         }


nome = input('Qual o seu nome? ')
print ('Olá, {}{}{} Boas vindas!'.format(cores['azul'],nome,cores['limpa']))

