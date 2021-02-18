numero = int(input('Digite um número: '))
fatorial = 1
primeiro = numero

while numero != 0:

    fatorial *= numero
    numero -= 1

print(f'{primeiro}! =', end=' ')
for i in range(primeiro, 0, -1):
    if i == 1:
        print(f'{i}', end='')
    else:
        print(f'{i}', end=' x ')
print(f' = {fatorial}')