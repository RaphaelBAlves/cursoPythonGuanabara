lista = []

while True:
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Este número já está na lista, digite outro.')
    else:
        lista.append(numero)
    opcao = input('Quer digitar outro número? [s/n]: ')
    if opcao == 'n':
        break

print(lista)
lista.sort()
print(lista)