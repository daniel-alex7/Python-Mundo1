lar = float(input('\033[31m Digite a largura da parede:  \033[m' ))
alt = float(input('\033[31m Digite o valor da altura da parede:  \033[m'))

area = lar * alt

lata = area / 2

print('A area da parede é {}m e vão precisar de {} latas de tintas para pinta-lá'.format(area,lata))