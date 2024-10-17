# Jokenpô
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
print('-=' * 11)
jogador = int(input('Qual é a sua jogada:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('O computador escolheu {}.'.format(itens[computador]))
print('Você escolheu ', end='')

if jogador == 0:
    print('PEDRA.')
    if computador == 0:
        print('Empate!')
    elif computador == 1:
        print('Você Perdeu!')
    elif computador == 2:
        print('Você Ganhou!')
elif jogador == 1:
    print('PAPEL.')
    if computador == 0:
        print('Você Ganhou!')
    elif computador == 1:
        print('Empate!')
    elif computador == 2:
        print('Você Perdeu!')
elif jogador == 2:
    print('TESOURA.')
    if computador == 0:
        print('Você Perdeu!')
    elif computador == 1:
        print('Você Ganhou!')
    elif computador == 2:
        print('Empate!')
else:
    print('uma OPÇÃO INVÁLIDA!')
