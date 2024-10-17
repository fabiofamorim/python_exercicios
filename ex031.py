#Cálculo de preço de viagem.
dist = float(input('Qual a distância da viagem?'))
print('Você está prestes a começar uma viagem de {} km(s).'.format(dist))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
'''
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
    '''
print('E o preço da sua passagem será de \033[34;40mR${:.2f}\033[m.'.format(preco))