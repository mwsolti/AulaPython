#Repetição sem Loop

list_aluno = ["Rosenildo","Juriscleudo","Ziraldo"]

list_media = [4,8,6]

cont =0
for media in list_media:

    if int(media) >= 7:
        print("O ALuno: "+list_aluno[cont] + " Passou" + " com a media: "+ str(media))
    elif int(media) >=5:
        print("O ALuno: "+list_aluno[cont] + " Recuperação" + " com a media: "+ str(media))
    else:
        print("O ALuno: "+list_aluno[cont] + " Reprovou" + " com a media: "+ str(media))
    
    cont +=1

#LIsta do exercicio 9
list_nomes = ["Ana","João","Juriscleido","Roberto","Ana"," Juriscleido","Tião","Jagunço","Juriscleida","Juriscleido","Roberto","Ana"," Juriscleido","Tião","Jagunço","Juriscleida","Juriscleido","Roberto","Ana"," Juriscleido","Tião","Jagunço","Juriscleida","Juriscleido","Roberto","Ana"," Juriscleido","Tião","Jagunço","Juriscleida"]