soma_idade = 0
idade_maior = 0
nome_mais_velho = ''
mulheres_menos_vite = 0

for i in range(4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite idade: '))
    soma_idade += idade
    sexo = str(input('Digite o sexo: ')).lower()
    if sexo == 'f' and idade < 20:
        mulheres_menos_vite += 1
    elif sexo == 'm':
        if idade > idade_maior:
            nome_mais_velho = nome

print(f'Média da idade do grupo: {soma_idade/4:.2f}')
print(f'Nome do homem mais velho: {nome_mais_velho}')
print(f'Mulheres com menos e 20 anos: {mulheres_menos_vite}')