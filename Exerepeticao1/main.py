'''
REPENQ1) Faça um algoritmo que calcule a multiplicação de dois números inteiros sem utilizar o operador “*”. Em vez disso, utilize apenas o operador de adição “+”. Para implementar esse algoritmo, devemos lembrar que qualquer multiplicação pode ser expressa por meio de somas. Por exemplo, o resultado da expressão 6 * 3 é o mesmo que 6 + 6 + 6 ou 3 + 3 + 3 + 3 + 3 + 3. Ou seja, soma-se um elemento com ele próprio o número de vezes do segundo elemento
'''
#Entradas
multiplicando = int(input('Digite um número para ser multiplicado: '))
multiplicador = int(input('Digite por qual número será multiplicado: '))

#Processamento
i = 0
resultado = 0
while i < multiplicador:
  resultado = resultado + multiplicando 
  i = i + 1

#Saída
print(f'O resultado da multiplicação de {multiplicando} X {multiplicador} é: {resultado}') 

