lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite o valor da altura da parede: '))

area = lar * alt

lata = area / 2

print('A area da parede é {}m e vão precisar de {} latas de tintas para pinta-lá'.format(area,lata))