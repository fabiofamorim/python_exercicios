#Tabuada.  Quando apresentar a tabuada de um número negativo encerre.
while True:
    n = int(input('Quer ver a tabuada de que número: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
    print('-' * 30)
print('Programa Tabuada Encerrado')
