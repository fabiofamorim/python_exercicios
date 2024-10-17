# Calculando formas de pagamento
print('{:=^40}'.format('Lojas Amorim'))

prod = float(input('Digite o valor do produto: '))
print('''Formas de Pagamento
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    total = prod - (prod * 10 / 100)
    print('Total com 10% de desconto: R$ {:.2f}.'.format(total))
elif opcao == 2:
    total = prod - (prod * 5 / 100)
    print('Total com 5% de desconto: R$ {:.2f}.'.format(total))
elif opcao == 3:
    parc = prod / 2
    print('Produto parcelado 2x s/ juros. Valor da parcela: R$ {:.2f}.'.format(parc))
elif opcao == 4:
    juros = prod + (prod * 20 / 100)
    print('Produto parcelado 3x ou mais. Valor total R$ {:.2f}, Valor total com Acréscimo R$ {:.2f}.'.format(prod, juros))
    parc = int(input('Sua compra será parcelada em quantas vezes?'))
    parcela = juros / parc
    print('Compra confirmada. {} parcelas de R$ {:.2f}.'.format(parc,parcela))
else:
    print('Opção inexistente!')
    