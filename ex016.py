# crie um programa que leia um número real e retorne sua parte inteira
from math import trunc
num = float(input('Digite um num: '))
print('O valor digitado{} e a sua porção inteira é {:.0f}'.format(num, trunc(num)))
