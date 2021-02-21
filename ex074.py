from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#maior = menor = 0
#cont = 1

print('Numéros sorteados: ', end='')

for pos, n in enumerate(numeros):

    if pos == 4:
        print(n, end='')
        print('')
    else:
        print(n, end=' - ')

print(f'Maior número: {max(numeros)}\nMenor número: {min(numeros)}')


'''
    if n > maior:
        maior = n

    if cont == 1:
        menor = n

    if n < menor:
        menor = n

    cont += 1
'''
