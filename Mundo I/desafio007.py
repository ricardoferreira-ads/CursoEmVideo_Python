'''Desenvolva um programa que leia duas notas do aluno e calucule e mostre a sua média'''

priNota = float(input('Insira a primeira nota do aluno(a): '))
segNota = float(input('Insira a segunda nota do aluno(a): '))
'''Duas Formas
Primeira solução:'''
res = (priNota + segNota) / 2
print('A media das notas obtidas pelo aluno(a) foi: {}'.format(res))

'''Segunda solucação:'''
print('A media das notas obtidas pelo aluno(a) foi: {}'.format((priNota + segNota)/2))