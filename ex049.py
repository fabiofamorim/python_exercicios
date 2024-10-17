# Tabuada

num = int(input('Digite um número para ver a sua tabuada:\n'))
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(num,c , num * c))
