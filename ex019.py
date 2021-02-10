from random import choice

alunos = []

for i in range(4):
    nome = input('Digite um nome: ')
    alunos.append(nome)

escolhido = choice(alunos)
print('Aluno escolhido para apagar o quadro: {}'.format(escolhido))