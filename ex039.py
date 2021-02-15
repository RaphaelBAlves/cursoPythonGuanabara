from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
sexo = input('Qual o seu sexo [m/f]: ')
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if sexo.lower() == 'm':
    if idade > 18:
        print(f'Já passou do tempo de você se alistar. Você tem {idade} anos. A idade certa é 18 anos.')
        print(f'Você está atrasado: {idade - 18} ano(s).')
        print(f'Você era para ter se alistado em: {ano_atual - (idade - 18)}.')
    elif idade == 18:
        print('Você está na idade certa para se alistar.')
    else:
        print('Você ainda não está no tempo de se alistar.')
        print(f'Falta(m) {18 - idade} ano(s).')
elif sexo.lower() == 'f':
    print('Você não precisa se alistar')
else:
    print('Confira o regulamento com as Forças Armadas.')
