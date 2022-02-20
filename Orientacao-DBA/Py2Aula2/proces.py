
from back import backEscola

def cadastra_aluno():
  nome = input("Digite o noem do Aluno: ")
  nota1 =float(input("Digite a nota 1: "))
  nota2 = float(input("Digite a nota 2: "))
  nota3 = float(input("Digite a nota 3: "))
  return  dict_aluno(nome,nota1,nota2,nota3 )

def dict_aluno(nome,nota1,nota2,nota3):
  escola = backEscola()
  dict_aluno = {}
  dict_aluno[nome] = escola.cauculaMedia(nota1,nota2,nota3)
  return dict_aluno