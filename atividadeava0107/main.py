'''
Instruções: Faça um programa que recebe vários números, calcule e mostre:
- a soma dos números digitados;
- a quantidade de números digitados;
- a média dos números digitados;
- o maior número digitado;
- o menor número digitado; 
- a média dos números pares;
- a porcentagem dos números ímpares entre todos os números digitados.
Finalize a entrada de dados com a digitação do número 30000.
'''
#Aresentação do Programa
print('''Digite vários números para ver:
- a soma dos números digitados;
- a quantidade de números digitados;
- a média dos números digitados;
- o maior número digitado;
- o menor número digitado;
- a média dos números pares;
- a porcentagem dos números ímpares entre todos os números digitados.''')
print('-*' * 30)
#Entradas
soma = 0
num = 0
num_dig = 0
maior = 0
menor = 0
qtde_par = 0
soma_par = 0
qtde_impar = 0
while True:
  #Cálculo Contador
  num_dig = num_dig + 1
  num = int(input(f'Digite o {num_dig}° número(ou 30000 para ver o resultado): '))
  #Condição para parar a solicitação de entradas
  if num == 30000:
    num_dig = num_dig -1
    break
  #Cálculo para obter a soma total
  soma = soma + num
  #Condição para descobrir o maior
  if num > maior:
    maior = num
  #Condição para descobrir o menor
  if num_dig == 1:
    menor = num
  else:
    if num < menor:
      menor = num
  #Condição para somar apenas os números pares
  if num % 2 == 0:
    qtde_par = qtde_par + 1
    soma_par = soma_par + num
  else:
    qtde_impar = qtde_impar + 1
#Cálculo para obter a média
media = soma / num_dig
#Cálculo para obter a media dos pares
media_par = soma_par / qtde_par
#Cálculo para obter pecentual de ímpares
perc_imp = qtde_impar * 100 / num_dig
print(f'''RESULTADOS
Soma dos números: {soma}
Quantidade de números: {num_dig}
Média dos números: {media}
Maior número: {maior}
Menor número: {menor}
Média dos números pares: {media_par}
Percentual de números ímpares: {perc_imp}%''')