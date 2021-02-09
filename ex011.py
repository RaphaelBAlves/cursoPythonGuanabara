altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
litros = area // 2
print('Área da parede: {} m2\nLitros de tinta para pintá-la: {:.0f} l'.format(area, litros))