d = int(input('Quantidade de dias alugados: '))
km = float(input('Quilometros percorridos: '))
valor = d * 60 + km * 0.15
print('Número de dias: {}, quilometros percorridos: {}.\nValor a ser cobrado: R$ {:.2f}.'.format(d,km,valor))