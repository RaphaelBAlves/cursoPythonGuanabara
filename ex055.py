maior = 0
menor = 0


for i in range(5):
 peso = float(input(f'Digite o peso {i+1}: '))
 if peso > maior:
     maior = peso
     if menor == 0:
         menor = peso
 if peso < menor:
     menor = peso

print(f'O maior peso digitado {maior}')
print(f'O menor peso digitado {menor}')

