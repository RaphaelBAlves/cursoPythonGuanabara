from datetime import date

maior_idade = 0
menor_idade = 0

for i in range(7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i+1}a pessoa: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'Você digitou {maior_idade}a pessoa maior de idade.')
print(f'Você digitou {menor_idade}a pessoa menor de idade.')