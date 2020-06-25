'''
Instruções: Faça um programa que leia um número não determinado de pares de valores [m,n], todos inteiros e positivos, um par de cada vez, e que calcule e mostre a soma de todos os números inteiros entre m e n (inclusive). A digitação de pares terminará quando m for maior ou igual a n.
'''
num_m = 0
num_n = 1
total = 0
while num_m < num_n:
  print(30 * '-*')
  print('Digite um intervalo para saber a soma dos números dentro dele.\nObs: Se você digitar o 1° número maior que o 2° número,\no programa será encerrado!!!')
  print(60 * '-')
  num_m = int(input('Digite um número inteiro e positivo qualquer: '))
  num_n = int(input('Digite outro número inteiro e positivo qualquer: '))
  if num_m >= num_n:
    break
  for i in range(num_m,num_n + 1):
    print(i, end=" ")
    total = total + i
  print(f'\nO total da soma de todos os números dentro do intervalo de {num_m} à {num_n}) é: {total}')
print(30 * '-!')
print(f'Você digitou o final do intervalo maior que o início!')
