# de um desconto de 5% no produto
num = float(input('Digite o valor do produto: '))
desc = num * 5 / 100
print('Valor do produto R$ {:.2f}\nValor do desconto R$ {:.2f}\nValor com o desconto{:.2f}'.format(num,  desc, num - desc))
