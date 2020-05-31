'''
Instruções: -Faça um programa em Python que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa;
b) quantos anos ela terá em 2050.
'''
#Entradas
from datetime import date
ano_nasc = int(input('Digite o ano que você nasceu(XXXX): '))
ano_atual = date.today().year

#Processamento
idade_atual = ano_atual - ano_nasc
idade_2050 = 2050 - ano_nasc

#Saída
print(f'Sua idade é {idade_atual} anos')
print(f'Em 2050 você terá {idade_2050} anos')
