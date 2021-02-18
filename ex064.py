soma = 0
quantidade = 0
numero = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        soma += numero
        quantidade += 1

print(f'Soma dos números digitados: {soma}\nQuantidade de números digitados: {quantidade}')