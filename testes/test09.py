print("\033[7;30m Olá mundo\033[m")

a= 3
b = 5
print("Os valore são \033[32m{}\033[m e \033[31m{}\033[m  ". format(a,b))



#Segunda Maneira
nome = 'Daniel'
print("Olá, Muito bem vindo, {}{}{}".format('\033[4;34m',nome,'\033[m'))


#Terceira maneira
nome = 'Daniel'

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'
         }
print("Olá, Muito bem vindo, {}{}{}".format(cores['amarelo'],nome,cores['limpa']))
print("Olá, Muito bem vindo, {}{}{}".format(cores['azul'],nome,cores['limpa']))