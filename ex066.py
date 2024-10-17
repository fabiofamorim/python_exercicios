''' Leia vários num inteiros pelo teclado. pare quando digitar 999, e no fim mostre quantos números foram digitados
e a soma entre eles(desconsiderando o flag)'''
n = soma = cont = 0
while n != 999:
    n = int(input('Digite um valor:  (999 para parar)'))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'{cont} foram digitados. E a soma dos valores foi {soma}.')