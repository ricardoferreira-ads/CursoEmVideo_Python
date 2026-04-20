'''Faça um programa que leia a altura e a largura de uma parede, 
calcule a area da parede e a quantidade de tinta necessaria para 
pintar a parede sabendo que cada litro de tinta pinta 2 metros 
quadados de area'''
v_altura = float(input('Insira o altura da parede: '))
v_largura = float(input('Insira o largura da parede: '))
v_redimneto_tinta = float(input('Cade litro de tinta rende quantos m2: '))
v_area = v_altura * v_largura


print('A area da total é de {} m2.\nPara pintar essa area será necessario {} lts de tinta'.format(v_area, (v_area / v_redimneto_tinta)) )


