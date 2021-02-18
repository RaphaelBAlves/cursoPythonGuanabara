vezes = int(input('Digite um número: '))
n1 = 0
n2 = 1
cont = 0

while cont < vezes:

    print(n1, end=' ')

    temp = n1 + n2
    n1 = n2
    n2 = temp

    cont += 1