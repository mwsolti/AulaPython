
def lista_compras():
    dict_lista_compras = {
        "Bacon": 2,
        "Queijo": 1,
        "Maionese": 3,
        "Leite": 2,
        "Feijão": 4,
        "Arroz":1
    }

    return dict_lista_compras



def pesquina_quantidade_nome(dict_lista_compras,nome):
    txt = "Quantidade do produto: "+nome+" é "+str(dict_lista_compras[nome])
    return txt


def  pesquisa_nomes_quantidade(dict_lista_compras,quantidade):

    list_nomes = dict_lista_compras.keys()
    list_nome_quantidade = []
    for nome in list_nomes:

        if dict_lista_compras[nome] == quantidade:
            list_nome_quantidade.append(nome)
    
    return list_nome_quantidade


def lista_produtos_quantidade(dict_lista_compras):
    list_nomes = dict_lista_compras.keys()

    for produto in list_nomes:
        print("Produto: "+produto+" : "+str(dict_lista_compras[produto]))



