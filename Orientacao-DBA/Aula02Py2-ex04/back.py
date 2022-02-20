from ast import Str

def pesquisa_idade_nome(dict_nome_idade,nome):
  
    txt ="A Idade do(a)>: "+nome+ " é "+str(dict_nome_idade[nome])

    return txt


def  pesquisa_nomes_idade(dict_nome_idade,idade):

    list_nomes = dict_nome_idade.keys()
    list_nome_idade = []
    for nome in list_nomes:

        if dict_nome_idade[nome] == idade:
            list_nome_idade.append(nome)
    
    return list_nome_idade


