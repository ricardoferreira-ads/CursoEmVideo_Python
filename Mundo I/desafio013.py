'''leia um salario e aplique aumento sobre ele'''
v_salario = float(input('Insira o valor do salario: '))
aliquota_reajuste = float(input('Insira a aliqota para reajuste: '))

v_reajuste = v_salario * (aliquota_reajuste /100)
novo_salario = v_salario + v_reajuste

print('O novo salario será: R$ {:.2f}'.format(novo_salario))
