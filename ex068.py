#Jogo Par ou Ímpar, interrompa quando jogador perder e mostre vitórias consecutivas que jogador conquistou.
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [ P / I ]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.',end=" ")
    print('DEU PAR!' if total % 2 ==0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu.')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
       if total % 2 == 1:
           print('Você Venceu!')
           v += 1
       else:
           print('Você perdeu!')
           break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')




