#Faça um programa que leia o tamanho de três retas e informe se pode fazer um triângulo.
print('Analisador de Triângulo.')
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;36mForma triângulo.\033[m')
else:
    print('\033[31mNão forma triângulo\033[m')
