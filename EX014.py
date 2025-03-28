cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         }


C = float(input('Digite temperatura em celsius: '))

F = (1.8 * C) + 32

print('Temperatura em fahrenheit é: {}°{}{}'.format(cores['azul'],F,cores['limpa']))