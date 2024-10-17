#Fazer o computador escolher nuero aleatório e usuário tentar descobrir

from random import randint
from time import sleep
computador = randint(0, 5) # este comando faz o sorteio.
print('-=-' * 10)
print('Vou pensar em um número de um a cinco. Tente adivinhar.:')
print('-=-' * 10)
jogador = int(input('Em que número pensei: ')) # Jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('\033[32;40mParabéns, você conseguiu me vencer!\033[m')
else:
    print('\033[30;41mVocê errou, eu pensei no número {} e não no número {}.\033[m'.format(computador, jogador))

