sala = float(input("Digite seu salário: "))

if sala >= 1250:
    aumento = (sala * 0.10) + sala
    print("Salário final é: {}".format(aumento))

else:
    aumento = (sala * 0.15) + sala
    print("Salário final é {}".format(aumento))