def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro.')
    else:
        print('Arquivo criado.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro.')
    else:
        print(a.read())
    finally:
        a.close()


def escreverArquivo(arquivo, nome, idade):
    try:
        a = open(arquivo, 'at')
    except:
        print('Deu erro.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao inserir nome.')
        else:
            print('Nome inserido com sucesso.')
        finally:
            a.close()


arquivo = 'teste.txt'

if arquivoExiste(arquivo):
    print('Arquivo existe.')
else:
    print('Arquivo não existe.')
    criarArquivo(arquivo)

lerArquivo(arquivo)

nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))

escreverArquivo(arquivo, nome, idade)

lerArquivo(arquivo)