from random import randint
lista = []


def sorteia():
    for i in range(5):
        numero = randint(1, 10)
        lista.append(numero)


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i

    return soma


sorteia()
print(lista)
resultado = somapar(lista)
print(f'A soma dos números pares na lista: {resultado}')