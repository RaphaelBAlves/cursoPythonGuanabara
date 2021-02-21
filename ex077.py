palavras = []
quant_a = 0
quant_e = 0
quant_i = 0
quant_o = 0
quant_u = 0

while True:
    palavra = str(input('Digite uma palavra: ')).lower()
    palavras.append(palavra)

    pergunta = input('Quer digitar outra? [s/n]: ')

    if pergunta == 'n':
        break

tupla = tuple(palavras)

for x in tupla:
    print(f'Palavra: {x} - Vogais: ', end='')

    for y in x:
        if y in 'a':
            print('a ', end='')
            #quant_a += 1
        if y in 'e':
            print('e ', end='')
            #quant_e += 1
        if y in 'i':
            print('i ', end='')
            #quant_i += 1
        if y in 'o':
            print('o ', end='')
            #quant_o += 1
        if y in 'u':
            print('u ', end='')
            quant_u += 1

    #print(f'a ({quant_a}) - e ({quant_e}) - i ({quant_i}) - o ({quant_o}) - u ({quant_u})')
    #quant_a = quant_e = quant_i = quant_o = quant_u = 0
    print('')
