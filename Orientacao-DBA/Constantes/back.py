from const import media_boa,media_regular


def status_media(media):
    if media >= media_boa:
        return "Passou"
    elif media >=media_regular:
        return "Recuperação"
    else:
        return "Reprovado"



