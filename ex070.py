total_gasto = 0
mais_de_mil = 0
mais_barato = 0
nome_barato = ''

while True:
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: R$ '))

    total_gasto += valor

    if valor > 1000:
        mais_de_mil += 1

    if mais_barato == 0:
        nome_barato = nome
        mais_barato = valor

    if mais_barato < valor:
        nome_barato = nome
        mais_barato = valor

    pergunta = str(input('Quer continuar comprando? [s/n]: ')).lower()
    if pergunta == 'n':
        break

print(f'Total gasto: {total_gasto}\nProdutos mais de R$ 1000: {mais_de_mil}\nProduto mais barato: {nome_barato}')