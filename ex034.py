#Conta de aumento de salário
sal = float(input('Qual o valor do seu salário?'))

if sal > 1250:
    novo = sal + (sal * 10 / 100)
    print('{:.2f}, salário com 10% de aumento.'.format(novo))
else:
    novo = sal + (sal * 15 / 100)
    print('{:.2f}, salário com aumento de 15%.'.format(novo))
print('Seu salário foi de \033[4mR$ {:.2f}\033[m para \033[4mR$ {:.2f}\033[m.'.format(sal, novo))
