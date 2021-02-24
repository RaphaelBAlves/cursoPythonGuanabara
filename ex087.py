matriz = []
numeros = []
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

for i in range(3):
    for j in range(3):
        numeros.append(int(input(f'Digite o número na posição [{i}][{j}]: ')))

    matriz.append(numeros[:])
    numeros.clear()

for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            soma_terceira_coluna += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior_segunda_linha:
                maior_segunda_linha = matriz[i][j]

for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]} ]', end='')
    print('')



print(f'Soma pares: {soma_pares}')
print(f'Soma terceira coluna: {soma_terceira_coluna}')
print(f'Maior número da segunda linha: {maior_segunda_linha}')