lista = []

for i in range(5):
    numero = int(input(f'Digite o {i + 1}o número: '))
    lista.append(numero)

maior = max(lista)
menor = min(lista)

print(f'Maior número: {maior}. Índice(s): ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}', end='... ')
print('')

print(f'Menor número: {menor}. Índice(s): ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}', end='... ')