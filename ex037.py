# Convertendo números
num = int(input('Digite um número inteiro: '))
print(''''Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binário é {}.'.format(num, bin(num)[2:]))
    '''' [2:] faz com que a posicao 0 e 1 nao aparecao. neste caso os indicadores 
    que aparecem antes do resultado.'''

elif opcao == 2:
    print('{} convertido para Octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Número inválido!')

