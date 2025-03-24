KM = float(input('Digite quantidade de KM percorridos: '))
dias = int(input('Digite a quantidade de dias a qual utilizou carro: '))

valor = (KM* 0.015) + (dias * 60)

print('O valor total à pagar é = R${:.2f}'.format(valor))