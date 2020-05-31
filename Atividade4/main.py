'''
Instruções: -Faça um programa em Python que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre a classificação dessa pessoa.
+--------------------+------------------------------------------------------+
|                    |                         Peso                         |
+--------------------+------------+---------------------------+-------------+
|      Altura        |   Até 60   | Entre 60 e 90 (inclusive) | acima de 90 |
+--------------------+------------+---------------------------+-------------+
| menores que 1,20   |      A     |             D             |      G      | 
+--------------------+------------+---------------------------+-------------+
| de 1,20 a 1,70     |      B     |             E             |      H      |
+--------------------+------------+---------------------------+-------------+
| maiores 1,70       |      C     |             F             |      I      |
+--------------------+------------+---------------------------+-------------+
'''
#Entradas
altura = float(input('Digite a altura em metros: ').replace(',','.'))
peso = float(input('Digte o peso em Kg:').replace(',','.'))
classific = 'indeterminado'

#Processamento
if altura < 1.20 and peso <= 60:
  classific = 'A'
elif altura < 1.20 and 60 < peso <= 90:
  classific = 'D'
elif altura < 1.20 and peso > 90:
  classific = 'G'
elif 1.20 <= altura < 1.70 and peso <= 60:
  classific = 'B'
elif 1.20 <= altura < 1.70 and 60 < peso <= 90:
  classific = 'E'
elif 1.20 <= altura < 1.70 and peso > 90:
  classific = 'H'
elif altura > 1.70 and peso <= 60:
  classific = 'C'
elif altura > 1.70 and 60 < peso <= 90:
  classific = 'F' 
elif altura > 1.70 and peso > 90:
  classific = 'I'

#Saída
print(f'A classificação da pessoa segundo altura e peso é: {classific}')
