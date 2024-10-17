#Sequencia de Finonacci
print('-=' * 30)
num = int(input('Quantos termos você quer mostrar?'))
print('-=' * 30)
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= num:
    t3 = t2 + t1
    print(' -> {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')