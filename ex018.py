from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))
sen = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}.'.format(angulo, sen))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}.'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}.'.format(angulo,tangente))