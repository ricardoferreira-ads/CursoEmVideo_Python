'''um professor que sortear um dos quatro alunos para apagar o quadro. 
faça um programa que ajude ele elendo o nome deles e escrevendo o nome do escolhido'''
import random
n1 = str(input('Digite o 1 nome: '))
n2 = str(input('Digite o 2 nome: '))
n3 = str(input('Digite o 3 nome: '))
n4 = str(input('Digite o 4 nome: '))
lista = [n1, n2, n3, n4]

print('O nome sorteado é: {}.'.format(random.choice(lista)))