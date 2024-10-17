# ler sexo até que resultado seja M ou F
sexo = str(input('Informe seu Sexo: [ M ou F ]\n')).strip().upper()[0] #[0]pega primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Opção inválida. Informe seu Sexo: [ M ou F ]\n')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))