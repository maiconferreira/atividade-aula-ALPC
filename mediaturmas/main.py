'''
REPENQ5) Faça um algoritmo que calcule a média de todas as turmas de uma escola. Considere como entradas o número de turmas e o número de alunos de cada turma. A média de cada turma deve ser apresentada, além da média geral, que será o resultado da média das turmas.
'''
#Entradas
turmas = int(input('Digite o número de turmas: '))
print()
t = 1
media_turma = 0
tot_geral = 0
media_geral = 0
#Processamento
while t <= turmas:
  alunos = int(input(f'Digite o número de alunos da turma {t}: '))
  print()
  a = 1
  tot_turma = 0
  while a <= alunos:
    nota = float(input(f'Digite a nota do {a}º aluno: '))
    tot_turma = tot_turma + nota
    media_turma = tot_turma / alunos
    a = a + 1
  print(f'A média da turma {t} é: {media_turma}\n')
  tot_geral = tot_geral + media_turma
  media_geral = tot_geral / turmas
  t = t + 1
print(f'A média geral da escola é: {media_geral}')
