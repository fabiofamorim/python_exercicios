# leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e calcule o comprimento da hipotenusa.
'''
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

from math import hypot

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente'))
hi = hypot(co, ca)
print('Comprimento da hipotenusa é {}'.format(hi))
