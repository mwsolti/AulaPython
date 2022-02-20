from back import backEscola

from proces import cadastra_aluno


op = ""
list_aluno = []
escola = backEscola()

while True:
  dict_aluno = cadastra_aluno()
  list_aluno.append(dict_aluno)
  op = input("Deseja continuar Cadastro? ")
  if op == "Não":
    break

for list_aluno in dict_aluno:
  for aluno in dict_aluno.keys():
    print("O Aluno: "+aluno+" Com media: "+str(dict_aluno[aluno])+ " "+ escola.statusMedia(dict_aluno[aluno])) 



