
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"r")
    list_itens_arquivo = arquivo.readlines()
    arquivo.close()
    return list_itens_arquivo




def compara_listas(list_compras, list_mercado):
    
    list_defrenca = []
    
    for item in list_mercado:
        
        if item not in list_compras:
            list_defrenca.append(item)
    

    return list_defrenca
    
    