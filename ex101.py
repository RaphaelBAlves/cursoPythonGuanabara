def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento

    if idade < 16:
        print(f'Com {idade} anos: voto negado.')
    elif (16 <= idade < 18) or idade > 70:
        print(f'Com {idade} anos: voto opcional.')
    else:
        print(f'Com {idade} anos: voto obrigatório.')


nascimento = int(input('Digite data de nascimento: '))

voto(nascimento)

