lista = []

for i in range(4):
    numero = int(input(f'Digite o {(i+1)}o número: '))
    lista.append(numero)

tupla = tuple(lista)
print(f'Você digitou os valores {tupla}')
numero_tres = tupla.count(3)

print(f'Quantas vezes apareceu o número "9": {tupla.count(9)}')
if  numero_tres != 0:
    print(f'Posição que foi digitado o primeiro valor "3": {(tupla.index(3)) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Números pares digitados: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')