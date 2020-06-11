'''
REPENQ8) Faça um algoritmo que leia o número de termos, determine e mostre os valores de acordo com a série abaixo:
Série = 2,7,3,4,21,12,8,63,48,16,189,192,32,567,768,64,...
'''
#Entradas
num_termos = int(input('Digite o número de termos da série: '))
x = 2
y = 7
z = 3

cont = 0
while cont < num_termos:
  cont = cont + 1
  if (cont - 1) % 3 == 0: 
    print(x)
    x = x * 2
  else: 
    if (cont - 2) % 3 == 0:
      print(y)
      y = y * 3
    else:
      print(z)
      z = z * 4
