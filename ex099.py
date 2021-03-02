def maior(lst):
    maior_numero = 0
    for i in lista:
        if i > maior_numero:
            maior_numero = i

    return maior_numero

lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    pergunta = input('Quer digitar outro número? [s/n]')
    if pergunta == 'n':
        break

resultado = maior(lista)

print(f'O maior número digitado: {resultado}')
