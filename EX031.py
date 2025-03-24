DisVia = float(input("Digite a distância da viagem: "))

if DisVia <= 200:
    prec = (200 - DisVia) * 0.50
    print("Valor total R${}".format(prec))


else:
    prec =  DisVia * 0.45
    print("Valor total R${}".format(prec))




