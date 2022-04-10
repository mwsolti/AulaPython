#Criando um Arquivo

# w - escrever(criar arquivo)
# r - ler o arquivo
# a - adicionar novos registros sem apagar anteriores

def cria_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"w")
    arquivo.close()

def escreve_arquivo(nome_arquivo,list_conteudo):
    arquivo = open(nome_arquivo,"a")
    for conteudo in list_conteudo:
        arquivo.writelines(str(conteudo)+"\n")
    arquivo.writelines("\n")
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"r")
    conteudo = arquivo.readlines()
    arquivo.close()
    return conteudo