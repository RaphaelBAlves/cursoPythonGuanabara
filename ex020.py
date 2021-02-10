from random import shuffle

alunos = []

for i in range(4):
    nome = input('Digite um nome: ')
    alunos.append(nome)

shuffle(alunos)

print('Ordem da apresentação dos alunos: ')

for i in alunos:
    print(i, end=', ')
