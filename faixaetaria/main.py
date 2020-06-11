'''
REPENQ7) Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
- A quantidade de pessoas em cada faixa etária
- A percentagem de pessoas em cada uma das faixas etárias, com relação ao total de pessoas, de acordo com a tabela abaixo:
Faixa Etária	Idade
1	Até 15 anos
2	De 16 a 30 anos
3	De 31 a 45 anos
4	De 46 a 60 anos
5	Acima de 61 anos
'''
#Entradas
cont = 0
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

while True:
  cont = cont + 1
  idade = int(input(f'Digite a idade da {cont}ª pessoa(Para sair digite "-1"): '))
  if idade == -1:
    break
  if idade <= 15:
    faixa1 = faixa1 + 1
  else:
    if idade >= 16 and idade <= 30:
      faixa2 = faixa2 + 1
    else:
      if idade >= 31 and idade <= 45:
        faixa3 = faixa3 + 1
      else:
        if idade >= 46 and idade <= 60:
          faixa4 = faixa4 + 1
        else:
          faixa5 = faixa5 + 1
tot_pessoas = cont -1
perc_f1 = faixa1 * 100 / tot_pessoas
perc_f2 = faixa2 * 100 / tot_pessoas
perc_f3 = faixa3 * 100 / tot_pessoas
perc_f4 = faixa4 * 100 / tot_pessoas
perc_f5 = faixa5 * 100 / tot_pessoas
print(50 * '-')
print(f'Foram {faixa1} pessoa(s) na faixa 1\nSendo {perc_f1:.2f}% do total de {tot_pessoas} pessoa(s) inserida(s)')
print(50 * '-')
print(f'Foram {faixa2} pessoa(s) na faixa 2\nSendo {perc_f2:.2f}% do total de {tot_pessoas} pessoa(s) inserida(s)')
print(50 * '-')
print(f'Foram {faixa3} pessoa(s) na faixa 3\nSendo {perc_f3:.2f}% do total de {tot_pessoas} pessoa(s) inserida(s)')
print(50 * '-')
print(f'Foram {faixa4} pessoa(s) na faixa 4\nSendo {perc_f4:.2f}% do total de {tot_pessoas} pessoa(s) inserida(s)')
print(50 * '-')
print(f'Foram {faixa5} pessoa(s) na faixa 5\nSendo {perc_f5:.2f}% do total de {tot_pessoas} pessoa(s) inserida(s)')
print(50 * '-')