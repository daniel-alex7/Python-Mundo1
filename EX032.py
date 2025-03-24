ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("Ano bissexto {}".format(ano))

else:
    print("Ano não bissexto")