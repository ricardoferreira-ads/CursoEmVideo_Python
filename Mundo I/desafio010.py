'''Crie um programa que converta reais para dolares'''
v_reais = float(input('Insira o valor em reais para conversão em dolares: '))
v_dolar = 3.27 

print('Com o valor inserido acima de R$ {} Reais, você pode comprar $ {:.2f} Dolares'.format(v_reais, v_reais/v_dolar))