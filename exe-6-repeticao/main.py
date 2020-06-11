'''	REPENQ6) Faça um programa que receba o valor do salário mínimo e
uma lista contendo a quantidade de quilowatts gasta por consumidor e o
tipo do consumidor (1-Residencial, 2-Comercial, 3-Industrial).
Calcule e mostre:
- O valor de cada quilowatt, sabendo que o quilowatt custa 1/8 do salário mínimo;
- O valor a ser pago por cada consumidor (conta final mais acréscimos),
considerando que o acréscimo é o mesmo da tabela a seguir:

	
Tipo	% de acréscimo sobre o valor gasto
1	5
2	10
3	15

- O faturamento geral da empresa
- a quantidade de consumidores que pagam entre R$ 500,00 e R$ 1000,00

Termine a entrada de dados quando a quantidade de quilowatts digitada for igual a zero.
'''
#Entradas
sal_min = float(input('Digite o valor do salário mínimo: R$'))
lista_cons = []
consumidor = 0
qtde = 0
faturamento = 0

#Processamento
#Cálculo do valor do quilowatts
val_kw = sal_min / 8
print(f'O valor do quilowatts é: R${val_kw}')

while True:
  #Entrada da quantidade de quilowatts gasta pelo consumidor
  kw_gasto_cons = float(input('Digite a quantidade gasta de quiliwatts pelo consumidor(Para sair digite 0): '))
  #Estrutura de decisão para parar sair do programa digitando 0
  if kw_gasto_cons == 0:
    break
  #Cálculo do valor total pago pela quantidade de quilowatts gasto
  val_tot_kw = val_kw * kw_gasto_cons
  print(f'O valor total sem o acréscimo é: R${val_tot_kw}')
  #Entrada do tipo de consumidor 
  tipo_cons = int(input('Digite o tipo de consumidor: '))
  #Estrutura de decisão para acréscimo segundo tipo de consumidor
  if tipo_cons == 1:
    val_pago = val_tot_kw + (val_tot_kw * 5 / 100)
  else:
    if tipo_cons == 2:
      val_pago = val_tot_kw + (val_tot_kw * 10 / 100)
    else:
      val_pago = val_tot_kw + (val_tot_kw * 15 / 100)
  print(f'O valor pago pelo consumidor é: R${val_pago}')
  #Estrutura de decisão para saber quantos consumidores pagaram entre R$500,00 e R$1000,00
  if val_pago >= 500 and val_pago <= 1000:
    qtde = qtde + 1
  #Cálculo do faturamento total da empresa
  faturamento = faturamento + val_pago
  #Adicionando valores na lista
  '''
  consumidor = consumidor + 1
  lista_cons.append(f'O consumidor {consumidor} pagou R${val_pago}') 
  '''
print(f'A quantidade de consumidores que pagam entre R$500,00 e R$1000,00 é: {qtde}')
#Estrututa para mostrar valores sobre consumidores guardados na lista
'''
for cons in lista_cons:
  print(cons)
'''
print(f'O faturamento da empresa será: R${faturamento}')
