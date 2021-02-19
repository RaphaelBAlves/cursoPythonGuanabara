soma = quantidade = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    else:
        soma += numero
        quantidade += 1

print(f'Quantidade de números digitados: {quantidade}\nSoma dos números: {soma}')