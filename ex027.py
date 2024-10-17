#informe o nome e em sequencia responde com o primeiro e o último nome.
n = str(input('Qual o seu nome:')).strip()
nome = n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))

