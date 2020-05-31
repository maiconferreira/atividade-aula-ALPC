'''
Instruções: -O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa em Python que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de imposto, calcule e mostre: 
a) o valor correspondente ao lucro do distribuidor;
b) o valor correspondente aos impostos;
c) o preço final do veículo.
'''
#Entradas
preco_fab = float(input('Digite o preço de fábrica do veículo: R$').replace(',',"."))
per_lucro = float(input('Digite o percentual de lucro do distribuidor: ').replace(',','.'))
per_impostos = float(input('Digite o percentual de impostos: ').replace(',','.'))

#Processamento
lucro_dist = (preco_fab * per_lucro) / 100
val_imp = (preco_fab * per_impostos) / 100
preco_final = preco_fab + lucro_dist + val_imp

#Saída
print(f'O lucro do distribuidor será de R${lucro_dist:.2f}')
print(f'O valor pago de impostos será de R${val_imp:.2f}')
print(f'O preço final do veículo será de R${preco_final:.2f}')
