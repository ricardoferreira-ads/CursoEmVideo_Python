'''faca um programa que que leia o comprimento do cateto oposto e do cateto adjecente, 
calcule e moste o comprimento da hipotenusa'''
from math import pow
from math import sqrt
from math import hypot
v_cateto_op = float(input('Insira o valor do cateto oposto: '))
v_cateto_ad = float(input('Insira o valor do cateto adjecente: '))
v_hipotenusa = sqrt( (pow(v_cateto_op, 2)) + (pow(v_cateto_ad, 2)))
print('O valor da hipotenusa é: {:.2f}'.format(v_hipotenusa))

'''segunda forma de resolver'''
print('a hipotenusa é: {}'.format(hypot(v_cateto_ad, v_cateto_op)))