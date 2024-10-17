a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a > b:
    print('{} é maior que o número {}.'.format(a, b))
elif b > a:
    print('{} é maior que o número {}.'.format(b, a))
else:
    print('Os números digitados foram iguais.')
