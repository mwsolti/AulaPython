
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


def cria_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"w")
    arquivo.close()


def escreve_arquivo(nome_arquivo,linha):
    arquivo = open(nome_arquivo,"a")
    arquivo.writelines(linha)
    arquivo.close()
    

def escreve_diferenca(nome_arquivo,list_diferenca):
    escreve_arquivo(nome_arquivo,"---------------------------------------- \n")
    
    for item in list_diferenca:
        escreve_arquivo(nome_arquivo,item)
    
    escreve_arquivo(nome_arquivo,"---------------------------------------- \n")
    
    