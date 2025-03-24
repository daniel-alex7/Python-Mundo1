velo = float(input("Digite a velocidade do carro: "))

if velo > 80:
    multa = (velo - 80) * 7
    print("Sua multa foi: R${}".format(multa))

else:
    print("Você está dentro do limite da via!")