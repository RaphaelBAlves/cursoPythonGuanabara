def area(largura, altura):
    return largura * altura

largura = float(input('Dite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))

resultado = area(largura, altura)

print(f'Área do terreno: {resultado:.1f} m2')