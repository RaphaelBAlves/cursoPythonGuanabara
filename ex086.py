matriz = []
numeros = []

for i in range(3):
    for j in range(3):
        numeros.append(int(input(f'Digite o número na posição [{i}][{j}]: ')))
    matriz.append(numeros[:])
    numeros.clear()

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^6}]', end='')
    print('')