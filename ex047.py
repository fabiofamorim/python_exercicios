#Conte de 0 a 50 mostrando apenas os números pares
for n in range(2, 51, 2):
    if n % 2 == 0:
        print(n, end='. ')

print('\nContagem Encerrada!')