
#Criando um Arquivo

# w - escrever(criar arquivo)
# r - ler o arquivo
# a - adicionar novos registros sem apagar anteriores

def cria_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"w")
    arquivo.close()

def escreve_arquivo(nome_arquivo,conteudo):
    arquivo = open(nome_arquivo,"a")
    arquivo.writelines(conteudo)
    arquivo.writelines("\n")
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"r")
    conteudo = arquivo.readlines()
    arquivo.close()
    return conteudo

# cria_arquivo("teste")

# escreve_arquivo("teste","Ola Alunos")

# escreve_arquivo("teste","Xau Alunos")

print(ler_arquivo("teste"))