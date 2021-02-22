lista = []
cont = 0

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    cont += 1
    pergunta = input('Quer digitar mais um número? [s/n]: ')
    if pergunta == 'n':
        break



print(f'Lista: {lista}')
print(f'Números digitados: {cont}')
lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')