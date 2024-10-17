'''Progressão aritimética. Leia o primeiro termo e a razão de uma PA.
No final, mostre os 1 0 primeiros termos.'''
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + ( 10 - 1) * razao  # 10 é por causa dos dez primeiros
for c in range(primeiro, decimo + razao, razao):
    print('{}'. format(c), end=' -> ')
print('Acabou!')