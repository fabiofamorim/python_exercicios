# Triângulos
l1 = float(input('Digite o lado 1 do triângulo em cm: '))
l2 = float(input('Digite o lado 2 do triângulo em cm: '))
l3 = float(input('Digite o lado 3 do triângulo em cm: '))

if l3 >= l1 + l2 or l1 >= l2 + l3 or l2 >= l1 + l3:
    print('Triângulo inexistente')
else:
    print('Os seguimentos acima PODEM FORMAR um TRIÂNGULO', end=' ')
    if l1 == l2 == l3:
        print('Equilátero.')
    elif l1 != l2 != l3 != l1:
        print('Escaleno.')
    else:
        print('Isósceles.')