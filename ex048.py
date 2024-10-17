#Calcule a soma de todos os n. ímpares multiplos de 3 que se encontram no intervalo entre 1 e 500
soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        contador += 1      # conta quantos números foram encontrados para soma
        soma += n      # soma = soma + n
print('A soma de todos os {} valores solicitados é {}.'.format(contador, soma))