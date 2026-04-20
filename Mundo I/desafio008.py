'''Escreva um programa que receba um numero em metro e exiba o seu valor convertido em centimetros e em milimetros'''
v_metro = float(input('Insira o valor em metros para convesão: '))
v_centimetros = v_metro*100
v_milimetros = v_metro*1000
print('O valor de {}mts, convertido para centimetro é de : {:.0f} cm.'.format(v_metro, v_centimetros))
print('O valor de {}mts, convertido para milimetros é de : {:.0f} mm.'.format(v_metro, v_milimetros))