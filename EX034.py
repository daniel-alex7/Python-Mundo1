cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'vermelho':'\033[31m',
         }


sala = float(input("Digite seu salário: "))

if sala > 1250:
    aumento = (sala * 0.10) + sala
    print("Salário final é: {}{}{}".format(cores['azul'],aumento,cores['azul']))

else:
    aumento = (sala * 0.15) + sala
    print("Salário final é {}{}{}".format(cores['verde'],aumento,cores['verde']))