altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
litros = area / 2
print('Área da parede: {:.3f} m2\nLitros de tinta para pintá-la: {:.4f} l'.format(area, litros))