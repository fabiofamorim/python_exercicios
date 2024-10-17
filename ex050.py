#leia números inteiros, mostre os pares e desconsidere os impares.
soma = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite o valor {}: '.format(c)))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você informou {} números PARES e a soma deles foi {}.'.format(count, soma))
