numero = int(input('Digite um número para saber a tabuada: '))

for i in range(0,11):
    print(f'{numero:2} X {i:2} = {numero * i:2}')