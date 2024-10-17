# Faça um programa que leia três numeros e informe qual deles é o maior e o menor deles.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

 #Verificando Menor
menor = a
if b < a and b < c:
     menor = b
if c < a and c < b:
    menor = c
print('Menor número digitado foi {}.'.format(menor))

#Verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Maior número digitado foi {}.'.format(maior))