
from funcao import media,status


nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
nota3 = float(input("Digite a Nota 3: "))


media = media(nota1,nota2,nota3)
status = status(media)


print (" --- Media: "+ str(media) +  "-----  \n "+ status)

