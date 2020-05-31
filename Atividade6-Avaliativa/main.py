'''
Instruções:
- Faça um programa em Python para resolver o problema. Uma empresa decidiu dar uma gratificação de Natal a seus funcionários, baseada no número de horas extras e no número de horas que o funcionário faltou ao trabalho. O valor do prêmio é obtido pela consulta a tabela que se segue na qual:

tempo = número de HORAS extras - (2/3 * (número de HORAS falta))

+--------------------------+--------------------------+
|   tempo (em minutos)     |       Prêmio (R$)        |
+--------------------------+--------------------------+
| >= 2.400 min             |        500,00            |
+--------------------------+--------------------------+
| 1800 min ○---○ 2.400 min |        400,00            |
+--------------------------+--------------------------+
| 1200 min •---○ 1.800 min |        300,00            |
+--------------------------+--------------------------+
|  600 min •---○ 1.200 min |        200,00            |
+--------------------------+--------------------------+
| < 600 min                |        100,00            |
+--------------------------+--------------------------+
'''
#Entradas
numHE = float(input('Digite o número de horas extras:'))
numHF = float(input('Digite o número de horas falta:'))

#Processamento
tempo = (numHE - (2/3 * (numHF))) * 60
if tempo >= 2400:
  premio = 500
else:
  if tempo >= 1800 and tempo < 2400:
    premio = 400
  else:
    if tempo >= 1200 and tempo < 1800:
      premio = 300
    else:
      if tempo >= 600 and tempo < 1200:
        premio = 200
      else:
        premio = 100

#Saída
print(f'A gratificação que o funcionário irá ganhar será: R${premio}')

