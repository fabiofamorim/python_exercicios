# leia o peso de cinco pessoas. e informe o maior e o menor peso lido.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(p)))
    if peso == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('{} kg = Maior peso informado.\n{} KG = Menor peso informado.'.format(maior, menor))