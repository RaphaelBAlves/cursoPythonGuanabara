primo = 0

numero = int(input('Digite um número: '))

for i in range(numero, 0, -1):
    if numero % i == 0:
        primo += 1

if primo == 2:
    print(f'{numero} é um número primo')
else:
    print(f'{numero} não é um número primo')