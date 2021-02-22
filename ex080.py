lista = []


for i in range(5):
    numero = int(input('Digite um número: '))
    if i == 0:
        lista.append(numero)

    if i == 1:
        if numero < lista[0]:
            lista.insert(0, numero)
        else:
            lista.insert(i, numero)

    if i == 2:
        if numero < lista[0]:
            lista.insert(0, numero)
        elif lista[0] <= numero <= lista[1]:
            lista.insert(1, numero)
        else:
            lista.insert(i, numero)

    if i == 3:
        if numero < lista[0]:
            lista.insert(0, numero)
        elif lista[0] <= numero <= lista[1]:
            lista.insert(1, numero)
        elif lista[1] <= numero <= lista[2]:
            lista.insert(2, numero)
        else:
            lista.insert(i, numero)

    if i == 4:
        if numero < lista[0]:
            lista.insert(0, numero)
        elif lista[0] <= numero <= lista[1]:
            lista.insert(1, numero)
        elif lista[1] <= numero <= lista[2]:
            lista.insert(2, numero)
        elif lista[2] <= numero <= lista[3]:
            lista.insert(3, numero)
        else:
            lista.insert(i, numero)




print(lista)