#calculo de salário e prestaçào de imóvel e tempo de pagamento. pagamento em no máximo 30 anos.
casa = float(input('Valor da casa: '))
sal = float(input('Valor do salário: '))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
min = sal * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end=" ")
print('a prestação será R$ {:.2f}.'.format(prestacao))

if prestacao <= min:
    print('Emprestimo Concedido.')
else:
    print('Emprestimo Negado')