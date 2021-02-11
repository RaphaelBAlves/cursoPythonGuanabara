frase = str(input('Digite uma frase: ')).strip()
frase = frase.lower()

print(f"Quantidade de letras 'a': {frase.count('a')}")
print(f'A letra "a" aparece pela primeira vez na posição: {frase.find("a") + 1}')
print(f'A letra "a" aparece pela última vez na posição: {frase.rfind("a") + 1}')
