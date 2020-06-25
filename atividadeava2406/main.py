'''
Instruções: Faça um programa que receba o salário de um funcionário chamado Carlos.    Sabe-se que outro funcionário, João, tem salário equivalente a um terço do salário de Carlos. Carlos aplicará seu salário integralmente na caderneta de poupança, que rende 2% ao mês, e João aplicará seu salário integralmente no fundo de renda fixa, que rende 5% ao mês. O programa deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencentea Carlos.
'''
sal_Carlos = float(input("Digite o salário de Carlos: R$"))
sal_Joao = sal_Carlos / 3
poup_Carlos = sal_Carlos
renfix_Joao = sal_Joao
meses = 0
while (poup_Carlos > renfix_Joao):
  poup_Carlos =  poup_Carlos + (poup_Carlos * 2 / 100)
  print(f'Poupança Carlos: {poup_Carlos}')
  renfix_Joao = renfix_Joao + (renfix_Joao * 5 / 100)
  print(f'Renda Fixa João: {renfix_Joao}')
  meses = meses + 1
print(f'O número necessário de meses para que João se iguale a Carlos é: {meses} meses')