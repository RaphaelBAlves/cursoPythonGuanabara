lista = [[], []]

for i in range(7):
    numero = int(input(f'Digite o {i+1}o número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()

print(f'Velores pares: {lista[0]}')
print(f'Valores ímpares: {lista[1]}')