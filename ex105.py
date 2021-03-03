def notas(* notas_alunos, situacao=False):

    maior = 0
    menor = 0
    soma = 0
    dados = {}

    for i, n in enumerate(notas_alunos):
        soma += n

        if i == 0:
            menor = n

        if n > maior:
            maior = n

        if n < menor:
            menor = n

    media = soma / len(notas_alunos)

    dados['total'] = len(notas_alunos)
    dados['maior'] = maior
    dados['menor'] = menor
    dados['media'] = media

    if situacao:
        if media > 8:
            dados['situacao'] = 'Excelente'
        elif 7 <= media <= 8:
            dados['situacao'] = 'Boa'
        else:
            dados['situacao'] = 'Vamos melhorar'

    return dados



resp = notas(10, 10, 10, situacao=True)

print(resp)