# Leia nome, idade e sexo de 4 pessoas. No fim mostre a média de idade, homem mais velho e qtas mulheres < 20
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('{}º Pessoa.'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [ M/F ]')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('Homem mais velho: {}\nSua idade: {}'.format(nomevelho, maioridadehomem))
print('{} pessoas tem menos de 20 anos.'.format(totmulher20))




