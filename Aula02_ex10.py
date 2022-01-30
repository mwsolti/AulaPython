list_alunos = ["Antonieta","Bruno","Zamira","Juriscleudo"]

list_notas_alunos = [[8,7,6],[7,8,5],[10,4,6],[3,4,5]]
cont = 0
for list_nota in list_notas_alunos:
    media = (sum(list_nota))/3
    print("O aluno: "+list_alunos[cont])
    print("Tem Media: "+str(media))
    cont +=1