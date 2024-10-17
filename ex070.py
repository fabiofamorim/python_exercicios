''' Qual é o total gasto na compra * Quantos produtos custam mais de 1000
Qual é o nome do produto mais barato? '''
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:    #se contador for 1 ou preco < o menor preco
        menor = preco
        barato = produto

    resp = " "
    while resp not in 'SN':
        resp = str(input('Quer continuar? [ S/ N ]')).strip().upper()[0]
    if resp == "N":
        break
print('{:-^40}'.format(" Fim do Programa "))
print(f'O total da compra foi R${total:10.2f}.')   # com 10 casas ao todo e dois pontos flutuantes
print(f'{totmil} produtos possuem valor acima de R$ 1000.00.')
print(f'O produto mais barato foi {barato} e seu custo é R$ {menor:.2f}.')
