dict_aluno = {}
list_notas = []

cont = 0
cont_nota= 0
while cont !=3 :
    cont +=1
    aluno = input("Digite o nome do Aluno: ")

    while cont_nota != 3:
        cont_nota +=1
        nota = float(input("Digite a Nota "+ str(cont_nota)+": " ))
        list_notas.append(nota)
    
    dict_aluno[aluno] = list_notas
    cont_nota = 0
    list_notas = []


list_alunos = dict_aluno.keys()

for aluno in list_alunos:
    media = (sum(dict_aluno[aluno]))/3

    if media >= 7:
        print("O ALuno: "+aluno+" Passou com Média: "+str(media))
    elif media >=5:
        print("O ALuno: "+aluno+" Está eem Recuperação com Média: "+str(media))
    else:
        print("O ALuno: "+aluno+" Reprovou com Média: "+str(media))