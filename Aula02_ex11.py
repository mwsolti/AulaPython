list_alunos = ["Antonieta","Bruno","Zamira","Juriscleudo"]
list_notas_alunos = [[8,7,6],[7,8,5],[10,4,6],[3,4,5]]
list_media = []

cont = 0
for list_nota in list_notas_alunos:
    media = (sum(list_nota))/3
    list_media.append(media)
   

for media in list_media:
    if media >=7:
        print("IO aluno: "+list_alunos[cont]+ " Passou com media: "+str(media))
    elif media >= 5:
         print("IO aluno: "+list_alunos[cont]+ " Está em Recuperação com media: "+str(media))

    else:
         print("IO aluno: "+list_alunos[cont]+ " Reprovou com media: "+str(media))
    
    cont +=1


