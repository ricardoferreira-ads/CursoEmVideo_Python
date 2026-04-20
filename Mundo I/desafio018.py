'''faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.'''
from math import cos, sin, tan, radians
x = float(input('Informe o angulo: '))
print("O angulo {} tem como:\nValor do seno: {:.2f}.\nValor do consseno: {:.2f}.\nValor da tangente {:.2f}.".format(x, sin(radians(x)), cos(radians(x)), tan(radians(x))))


