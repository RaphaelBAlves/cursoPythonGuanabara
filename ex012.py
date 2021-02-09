produto = float(input('Digite o valor do produto em R$: '))
valor = produto - ((produto * 5) / 100)
print('Produto com desconto de 5%: R$ {}'.format(valor))