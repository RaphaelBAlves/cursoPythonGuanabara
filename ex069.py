maior = homens = mulheres = 0


while True:
    idade = int(input('Digite uma idade: '))

    while True:
        sexo = str(input('Digite o sexo [m/f]: ')).lower()
        if sexo == 'm' or sexo == 'f':
            break

    if sexo == 'f' and idade < 20:
        mulheres += 1

    if sexo == 'm':
        homens += 1

    if idade > 18:
        maior += 1

    while True:
        pergunta = str(input('Quer continuar? [s/n]: ')).lower()
        if pergunta == 'n' or pergunta == 's':
            break

    if pergunta == 'n':
        break


print(f'Pessoas maiores de 18 anos: {maior}\nHomens cadastrados: {homens}\nMulheres com menos de 20 anos: {mulheres}')