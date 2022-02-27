
def media(nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    return media

def status(media):
    txt = "Reprovado"
    if media>=7:
        txt = "Passou"
    elif media >=5:
        txt = "Recuperação"

    return txt


#Postgres
#ElasticSearch