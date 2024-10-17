#Jogo de adivinhação. Descubra o número que o computador escolheu entre 1 e 10.
from random import randint
computador = randint(0, 11) # este comando faz o sorteio.
print('''Sou seu computador...
acabei de pensar em um número entre 1 e 10.
Será que você consegue adivinhar qual foi?''')
contador = 0
acertou = False

while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    contador += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Hum... O número que pensei é maior!.')
        elif jogador > computador:
            print('Hum... O número que pensei foi menor')

print('Parabéns! Você acertou depois de {} tentativas.'.format(contador))