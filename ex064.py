'''Tratando vários valores - crie um programa que leia números inteiros e só pare com o valor 999.
No fim, conte quantos números foram digitados e a soma entre eles(exceto flag).'''
n = cont = soma = 0
n = int(input('Digite um número ou 999 para parar:'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número ou 999 para parar:'))
print('Você digitou {} tantos números e a soma entre eles foi {}.'.format(cont,soma))