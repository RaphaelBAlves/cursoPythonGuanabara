from math import hypot
cat_opos = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(cat_opos,cat_adj)
print('Hipotenusa: {:.2f}'.format(hipotenusa))