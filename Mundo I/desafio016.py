'''crie um programa que leia um numero real epelo teclado e mostre na tela sua porção  inteira'''
# import math 
from math import trunc
num = float(input('Digite um numero Real: '))
print('A parte inteira do número {} é: {}'.format(num, trunc(num)))


