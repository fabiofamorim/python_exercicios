# CRIE O PROGRAMA E DIGA SE ELE TEM 'SILVA'NO NOME
nome = str(input('Digite seu nome:')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))