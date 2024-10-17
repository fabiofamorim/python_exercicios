#Simulador de caixa eletrônico. OBS Considere que o caixa possua cédulas de R$ 50, R$20, R$10 e R$1.

print("=" * 30)
print('{:^30}'.format('BANCO CEV'))
print("=" * 30)
valor = int(input('Que valor deseja sacar: R$ '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        print(f'Total de {totalcedula} cédulas de R$ {cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total <= 0:
            break
print('=' * 30)
print('Volte Sempre!')
