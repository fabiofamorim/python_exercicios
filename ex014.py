# Conversão de temperatura
c = float(input('Valor da temperatura em C°: '))
f = ((9 * c) / 5) + 32
print('\033[34m{} C°\033[m é igual a \033[34m{} F°\033[m.'.format(c,f))