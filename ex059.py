#Leia dois números e mostre um menu. Depois faça a opção selecionada
num1 = int(input('Digite um número: '))
num2= int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior Número
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')
    opcao = int(input('Qual a sua opção?'))
    if opcao == 1:
        resultado = num1 + num2
    elif opcao == 2:
        resultado = num1 * num2
    elif opcao == 3:
        if num1 > num2:
            resultado = num1
        elif num1 < num2:
            resultado = num2
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Finalizado')
    else:
        print('Opção inválida')
    print('Resultado = {}'.format(resultado))
    print('-='*10)
print('Fim do programa')