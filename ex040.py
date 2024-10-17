# Leia as notas e informe o status do candidato.
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1+ n2) / 2

print('De acordo com as notas {:.1f} e {:.1f} o aluno obteve a média de {:.1f}: '.format(n1, n2, media))
print('Status do aluno: ')
if media < 5.0:
    print('Reprovado!')
elif media >= 5 and media < 7:
    print('Recuperação!')
elif media >= 7.0:
    print('Aprovado!')

