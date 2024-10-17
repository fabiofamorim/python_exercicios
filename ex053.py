# Detector de Palíndromo (A palavra é a mesma escrevendo de trás pra frente?)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Divide as palavras da frase retirando os espaços emtre elas
junto = ''.join(palavras) # junta as palavras removendo o espaço entre elas
inverso = ''

#inverso = junto[::-1]  # o exercicio poderia ser feito apenas com isso e sem o for.

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)

if inverso == junto:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
