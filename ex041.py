from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Categoria MIRIM')
    print(f'Idade: {idade} anos')
elif idade <= 14:
    print('Categoria INFANTIL')
    print(f'Idade: {idade} anos')
elif idade <= 19:
    print('Categoria JÚNIOR')
    print(f'Idade: {idade} anos')
elif idade <= 20:
    print('Categoria SÊNIOR')
    print(f'Idade: {idade} anos')
else:
    print('Categoria MASTER')
    print(f'Idade: {idade} anos')

