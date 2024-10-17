'''Crie um programa que leia a idade e sexo de várias pessoas. a cada pessoa cadastrada,
o programa pergunta se quer ou nao continuar. Quantos > 18, qtos homens cadastrados e
quantas mulheres <20'''
tot18 = toth = totm = 0
while True:
    idade = int(input('Idade:'))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1

    if sexo == "M":
        toth += 1

    if sexo == "F" and idade < 20:
        totm += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar: [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E o total de mulheres é de {totm}.')
