'''O professor do desafio anterior deve sortear as orde de apresentação dos trabalhos dos alunos. 
faça um programa  que leia o nome e mostre a ordem de sorteio para apresentação'''
from random import shuffle

n1 = str(input('Digite o 1 nome: '))
n2 = str(input('Digite o 2 nome: '))
n3 = str(input('Digite o 3 nome: '))
n4 = str(input('Digite o 4 nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentacao é: {}'.format(lista))