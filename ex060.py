#Cálculo Fatorial
''' Forma 1 de se fazer
from math import factorial
n = int(input('Digite um número para calcular seu fatorial? '))
f = factorial(n)
print('O Fatorial de {} é {}.'.format(n,f)) '''
from time import sleep

n = int(input('Digite um número para calcular seu fatorial? '))
c = n
f = 1
print('Calculando {}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end=" ")
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c  # f = f * c
    c -= 1
sleep(0.5) # tempo em segundo
print('{}'.format(f))
