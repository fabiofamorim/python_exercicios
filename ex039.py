# Leia ano de nascimento e informe alistamento militar.
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento:\n'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Aliste-se imediatamente!')
elif idade > 18:
    saldo = 18 - idade
    ano = saldo + atual
    print('Aliste-se imediatamente. Serviço militar obrigatório em atraso.')
    print('O ano do seu alistamento foi {}.'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Faltam {} para o seu alistamento.'.format(saldo))
    print('Você deve se alistar no ano de {}.'.format(ano))
