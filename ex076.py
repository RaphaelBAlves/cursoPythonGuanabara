lista = []

while True:

    nome_produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input(('Digite o preco do produto: ')))
    lista.append(nome_produto)
    lista.append(preco)

    pergunta = str(input('Deseja continuar? [s/n]: ')).strip().lower()
    if pergunta == 'n':
        break

tupla = tuple(lista)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
n = 0
p = 1
while n < len(tupla):
    print(f'{tupla[n]:.<20}R$ {tupla[p]:5.2f}')
    n += 2
    p += 2

