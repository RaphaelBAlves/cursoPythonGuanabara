frase = str(input('Digite uma frase: ')).strip().lower()

frase_lista = list(frase)

while ' ' in frase_lista:
    frase_lista.remove(' ')

copia = frase_lista[:]
copia.reverse()

if frase_lista == copia:
    print(f"'{frase}' <-- é um palíndromo")
else:
    print(f"'{frase}' <-- não é um palíndromo")
