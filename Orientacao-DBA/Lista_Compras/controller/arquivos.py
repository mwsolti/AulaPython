#Funções de manipulação dos arquivos(banco de Dados)


def cria_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"w")
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"r")
    list_dados_arquivo = arquivo.readlines()
    arquivo.close()
    return list_dados_arquivo

def escreve_arquivo(nome_arquivo, list_dados):
    arquivo = open(nome_arquivo,"a")

    for item_lista in list_dados:
        arquivo.writelines(str(item_lista)+"\n")
    
    arquivo.close()