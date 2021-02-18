soma = 0
contador = 0
maior = 0
menor = 0
pergunta = 's'

while pergunta != 'n':
    numero = int(input('Digite um número: '))

    soma += numero
    contador += 1
    if numero > maior:
        maior = numero
        if menor == 0:
            menor = numero

    if numero < menor:
        menor = numero

    pergunta = str(input('Quer continuar a digitar [s/n]: ')).strip().lower()

print(f'Média: {soma/contador}\nMaior número digitado: {maior}\nMenor número digitado: {menor}')