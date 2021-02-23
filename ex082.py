lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    pergunta = input('Quer continuar? [s/n]: ')
    if pergunta == 'n':
        break

lista_pares = []
lista_impares = []

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(f'Lista original: {lista}')
print(f'Lista par: {lista_pares}')
print(f'Lista ímpar: {lista_impares}')