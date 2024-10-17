# Progressão aritimética com contador
from time import sleep

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('primeiro termo: '))
razao = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(' {} -> '.format(termo), end='')
        termo += razao
        cont += 1
    sleep(0.5)
    print('Pausa')
    mais = int(input('Deseja acrescentar mais quantos termos? '))
sleep(0.5)
print('Fim')
sleep(0.5)
print('Progressão realizada com {} termos mostrados.'.format(total))