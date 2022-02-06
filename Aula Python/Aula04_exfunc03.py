def dados_casdastrados():
    dict_dados = {
        1: "Josivaldo",
        2: "Juriscleudo",
        3: "Antonia",
        4: "Ronaldo"
    }

    return dict_dados


def verifica_dados(codigo):
    dict_cadastro= dados_casdastrados()
    list_codigo = dados_casdastrados().keys()

    if codigo in list_codigo:
        print(dict_cadastro[codigo])
    else:
        print("Coditgo Não Cadstrado")


codigo = int(input("Digite um COoigo: "))

verifica_dados(codigo)
