from utilidades import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade do preço: {moeda.metade(preco)}')
print(f'O dobro do preço: {moeda.dobro(preco)}')
print(f'Aumento de 10% sobre o preço: {moeda.aumentar(preco, 10)}')
print(f'Redução de 13% sobre o preço: {moeda.diminuir(preco, 13)}')