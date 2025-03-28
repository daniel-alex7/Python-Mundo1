P = float(input('\033[33m Digite o preço do produto: \033[m'))
desconto = P - (P * 0.05)

print('Com o desconto de 5% fica = R${:.2f}'.format(desconto))