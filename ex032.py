# Faça um programa que diga se o ano é bissexto
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analizar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} NÃO é Bissexto'.format(ano))