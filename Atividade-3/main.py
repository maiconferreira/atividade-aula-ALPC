'''
Instruções: -Faça um programa em Python que receba três números, apresente os três números em ordem crescente.
'''
'''
#Código com sort()
#Entradas
num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))

#Processamento
numeros = [num1, num2, num3] 
numeros.sort()

#Saída
print(numeros)
'''
#Código com estrutura de decisão
#Entradas
num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))

#Processamento
if num1 < num2 and num1 < num3 and num2 < num3:
  print(f'O menor número é o {num1}, seguido do {num2} e por último o {num3}')
elif num1 < num2 and num1 < num3 and num3 < num2:
  print(f'O menor número é o {num1}, seguido do {num3} e por último o {num2}')
elif num2 < num1 and num2 < num3 and num1 < num3:
  print(f'O menor número é o {num2}, seguido do {num1} e por último o {num3}')
elif num2 < num1 and num2 < num3 and num3 < num1:
  print(f'O menor número é o {num2}, seguido do {num3} e por último o {num1}')
elif num3 < num1 and num3 < num2 and num1 < num2:
  print(f'O menor número é o {num3}, seguido do {num1} e por último o {num2}')
else:
  print(f'O menor número é o {num3}, seguido do {num2} e por último o {num1}')

