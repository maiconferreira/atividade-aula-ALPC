'''
REPENQ2) Faça um algoritmo que leia um número inteiro e calcule o seu fatorial. Se o número for negativo, informe que o valor é inválido. Sabemos que o fatorial de um número n, representado por n!, é dado por:
n * (n-1) * (n-2) * ... * 1, para n > 0 e n! = 1 para n = 0
'''
#Entradas
num = int(input('Digite um número para ver seu fatorial: '))

#Processamento
n = num
f = num
if num != 0:
  while num > 1:
    print(f'{num} * ', end='')
    num = num - 1
    n = n * num
  print(f'{num}')
  print(f'O fatorial de {f} é: {n}')
else:
  print(f'O fatorial de 0 é: 1')