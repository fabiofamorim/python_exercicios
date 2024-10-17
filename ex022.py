'''
todas as letras maiusculas e minusculas, quantas letras tem ao
todo sem espaço e quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o seu nome:')).strip() # funcao strip retira os espacos antes e depois do str
print('Analisando seu nome')
print('Seu nome em maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
# o menos nome.count retira o espaço entre as palavras
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() # joga os nomes inteiros dentro de uma lista
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
# separa[0] indica o primeiro nome da lista criada no split


