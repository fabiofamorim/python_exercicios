''' Crie um programa que leia vários num int pelo teclado e mostre -> média de todos, maior e menor valor lido.
e pergunte se usuário quer continuar digitando valores.'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    quant += 1
    if quant ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {:.2f}.'.format(quant,media))
print('O maior número é {} e o menor número é {}.'.format(maior, menor))