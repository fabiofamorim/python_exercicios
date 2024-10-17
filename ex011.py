#lata de tinta cobre dois metros quadrados. de quanto precisa pra cobrir a area?
lar = float(input('Digite a largura em metros: '))
alt = float(input('Digite o valor da altura em metros: '))
area = lar * alt

print('Para cobrir a área de {}m² precisa de {} latas'.format(area, (area // 2) + (area % 2) ))