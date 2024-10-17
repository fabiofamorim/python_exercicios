sal = float(input('Digite o valor do seu salário: '))
aumento = sal + (sal * 15 / 100)
print('Salário real = R$ {:.2f}\nSalário com aumento de 15% = R$ {:.2f}'.format(sal, aumento))
