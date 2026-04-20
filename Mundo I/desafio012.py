'''faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto'''

v_produto = float(input('Insira o valor do produto para o desconto: '))
porc_desconto = float(input('Valor de desconto: '))
v_desconto = v_produto * (porc_desconto/100 )
preco_c_desconto = v_produto - v_desconto
print('O novo valor a pagar com desconto de {:.0f}% é de R$ {:.2f}.'.format(porc_desconto, preco_c_desconto))