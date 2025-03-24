n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite o próximo número: "))

#MAIOR
if n1 > n2 and n1 > n3:
    print("{} Maior número.".format(n1))

elif n2 > n3 and n2 > n1:
        print("{} Maior número.".format(n2))

else:
            print("{} Maior número.".format(n3))

#MENOR
if n1 < n2 and n1 < n3:
    print("{} Menor número.".format(n1))

elif n2 < n3 and n2 < n1:
        print("{} Menor número.".format(n2))

else:
            print("{} Menor número.".format(n3))