# Qual a velocidade média do carro.
vel = float(input('Qual é a velocidade atual do carro:'))
if vel > 80:
    print('\033[4;30;41mMULTADO. VOCÊ EXCEDEU O LIMTE DE 80 KM/H.\033[m')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}.'.format(multa))
print('Tenha um bom dia. Dirija com segurança.')