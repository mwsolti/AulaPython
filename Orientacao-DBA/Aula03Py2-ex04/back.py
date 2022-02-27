def cadastra_lista_compras():
    nome_produto = ""
    list_produtos = []

    while True:
        nome_produto = input("Digite o nome do Produto ou Sair para encerrar: ")

        if nome_produto == "Sair":
            break
        else:
            qt_produto = input("Digite a quantidade deste produto: ")
            preco_produto = input("Digite o Preço do Produto: ")

            list_produtos.append(nome_produto +" "+qt_produto+" "+preco_produto)

    return list_produtos



def cria_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"w")
    arquivo.close()

def escreve_arquivo(nome_arquivo,conteudo):
    arquivo = open(nome_arquivo,"a")

    for item in conteudo:
        arquivo.writelines(item)
        arquivo.writelines("\n")
        
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,"r")
    conteudo = arquivo.readlines()
    arquivo.close()
    return conteudo
